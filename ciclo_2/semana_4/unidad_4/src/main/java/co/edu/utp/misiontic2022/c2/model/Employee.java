package co.edu.utp.misiontic2022.c2.model;

public class Employee {
    
    private Integer employee_id;
    private String first_name;
    private String last_name;
    private String email;

    public Employee() {

    }

    public Employee (Integer employee_id, String first_name, String last_name, String email){
        this.employee_id = employee_id;
        this.first_name = first_name;
        this.last_name = last_name;
        this.email = email;
    }

    public Integer getEmployee_id(){
        return this.employee_id;
    }

    public void setEmployee_id(Integer employee_id){
        this.employee_id = employee_id;
    }

    public String getFirst_name() {
        return this.first_name;
    }

    public void setFirst_name(String first_name){
        this.first_name = first_name;
    }

    public String getLast_name(){
        return this.last_name;
    }

    public void setLast_name(String last_name){
        this.last_name= last_name;
    }

    public String getEmail(){
        return this.email = email;
    }

    public void setEmail(String email){
        this.email = email;
    }

    public String toString(){
        return "(" + this.getEmployee_id() + ") " + this.first_name + " " + this.last_name;
    }
    
}
