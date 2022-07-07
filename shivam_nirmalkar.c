#include<stdio.h>
int main(){
    char name[50];
    printf("Enter a name");
    scanf("%s",&name);
    switch (name[50]){
        case "SHIVAM":
        printf("name is equales to SHIVAM");
        case "GAURAV":
        printf("name is equales to GAURAV");
        case "SANDIP":
        printf("name is equales to SANDIP");
        default;
        printf("name is not equales to SHIVAM, GAURAV or SANDIP ");
}
return 0;
}