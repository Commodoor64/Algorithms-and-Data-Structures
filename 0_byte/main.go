package main

import (
	"fmt"
	"os"
	"os/exec"
	"io/ioutil"
	"sort"
	"log"
	"strings"
	"time"
)

func main() {
	var folders []string

	files, err := ioutil.ReadDir("code")
	
	if err != nil {
		log.Fatal(err)
	}

	for _, file := range files {
		if file.IsDir() {
			folders = append(folders, file.Name())
		}

	}
	
	
	sort.Strings(folders)

	f, err := os.Create("code/run.go")

	if err != nil {
        log.Fatal(err)
    }

    defer f.Close()

	for i:=0;i<len(folders);i++{
		folders[i] = fix(folders[i])
	
	}
	
	for _, line:= range folders{

		_, err2 := f.WriteString(line + "\n")

		if err2 != nil {
			log.Fatal(err2)
		}
	
	
	}


	c := exec.Command("go","run", "code/run.go")
	c.Stdout = os.Stdout
	c.Stderr = os.Stderr
    if err := c.Run(); err != nil { 
        fmt.Println("Error: ", err)
    }
	
	os.Remove("code/run.go") //don't know why this isnt working
}


func fix(line string) string{
	var newline string
	var start bool
	for i:=0; i <len(line); i++{

		if i == 0{
		
		}else if line[i] == '_' && start == false{
			newline += " "
		}else{
			newline += string(line[i])
			start = true
		}
		
	}

	line = newline
	line = strings.Replace(line, "{col}", ":", -1)
	line = strings.Replace(line, "{slash}", "/", -1)
	line = strings.Replace(line, "{star}", "*", -1)
	line = strings.Replace(line, "{quote}", string('"'), -1)
	line = strings.Replace(line, "{leftcarrot}", "<", -1)
	line = strings.Replace(line, "{rightcarrot}", ">", -1)
	return line
}

