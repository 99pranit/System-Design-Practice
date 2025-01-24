# CREATE Statement Generator

### **M3: Meta-Meta Model**

M3 = {U, V, e, 𝚺, L}

- **U (node - entity):** {Student, Course}  
- **V (node - relation):** {Takes}  
- **e (edge between U and V):** {(Student, Takes), (Takes, Course)}  
- **𝚺 (domain of attributes):** {Sid, Sname, Cid, Cname}  
- **L (attribute of entity U and relation V):**
  - L(Student): {Sid, Sname}  
  - L(Course): {Cid, Cname}  
  - L(Takes): {Sid, Cid}  

  **Rules:**  
  - ∀x: x ∈ L(Student), Student is unique  
  - ∀x: x ∈ L(Course), Course is unique  
  - Ǝx: x ∈ L(Student) → L(Course)  

---

## Key Functions Overview

### **define_entity()**
- Initializes entity attributes.  
- Collects attributes for entities, including names, data types, and constraints.  

### **check_normal_form1()**
- Verifies compliance with the First Normal Form (1NF) by ensuring no repeating groups exist.  

### **cardinality()**
- Determines the relationship type based on cardinality values (n and m) and invokes the respective relationship function:
  1. **relation_1_1():** Defines a 1:1 relationship and returns an adjacency matrix.  
  2. **relation_1_n():** Defines a 1:N relationship and returns an adjacency matrix.  
  3. **relation_n_1():** Defines an N:1 relationship and returns an adjacency matrix.  
  4. **relation_n_m():** Defines an N:M relationship and builds a bridge table.  

### **build_bride_table()**
- Creates a bridge table for many-to-many relationships.  
- Ensures the presence of Primary Key (PK) and Foreign Key (FK) constraints.  

### **generate_create_statements()**
- Generates SQL `CREATE TABLE` statements.  

---

## Workflow

1. **define_entity():**  
   Ensures M3 requirements are input by the user.

2. **check_normal_form1(), cardinality(), build_bride_table():**  
   Internally build the M2 meta model.

3. **main():**  
   Acts as the central method to guide the user through defining entities, relationships, and generating the final schema (M1).  

