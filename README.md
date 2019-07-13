# space-angel

## Git Process
``` mermaid
graph TD
A("begin iteration")                            --> B
B("checkout (branch)-angel")                    --> C
B --"Exception[ (branch)-angel *not found* ]"   --> B.1
B.1("find common ancestor [branch and origin]") --> B.2
B.2("create angel branch [ (branch)-angel ]")   --> B
C("find common ancestor [ branch and angel ]")  --> D
D("merge previous ancestor [branch to angel]")  --> E
E("process all gates")                          --> F
F("save & commit the results ")                 --> H("end iteration")
```