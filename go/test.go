package main
import "fmt"

func main() {
    var n, m int;
    fmt.Scan(&n)
    fmt.Scan(&m)
    
    for i:=0; i < n; i++{
        for j:=0; j < m; j++{
            fmt.Print("[*]")
        }
        fmt.Println();
    }
}
