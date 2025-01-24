import pandas as pd

# Define the database class
class database:
    def __init__(self, e1_attribute_name=[], e1_data_type=[], e1_constraint=[],\
                 r_attribute_name=[], r_data_type=[], r_constraint=[],\
                e2_attribute_name=[], e2_data_type=[], e2_constraint=[]):
        # Initialize class attributes to store entity and relationship details
        self.e1_attribute_name = e1_attribute_name
        self.e1_data_type = e1_data_type
        self.e1_constraint = e1_constraint
        self.r_attribute_name = r_attribute_name
        self.r_data_type = r_data_type
        self.r_constraint = r_constraint
        self.e2_attribute_name = e2_attribute_name
        self.e2_data_type = e2_data_type
        self.e2_constraint = e2_constraint

    # Define entity 1 attributes
    def define_entity1(self, e1_attribute_name=[], e1_data_type=[], e1_constraint=[]):
        n_attribute = int(input("Enter the number of attributes in entity 1: "))
            
        # Ensure number of attributes is positive
        if n_attribute <= 0:
            print("The number of attributes must be greater than 0.")
            return
        
        # Collect attribute details for entity 1
        for i in range(n_attribute):
            print(f"\nEnter details for attribute {i + 1}:")
            attribute_name = input("Attribute Name: ").strip()
            data_type = input("Data Type (e.g., INT, VARCHAR): ").strip()
            constraint = input("Key Constraint (e.g., PK, FK, leave blank for none): ").strip().lower()
            
            # Append attribute details to lists
            self.e1_attribute_name.append(attribute_name)
            self.e1_data_type.append(data_type)
            self.e1_constraint.append(constraint or "None")
        
        # Create and display DataFrame for entity 1
        e1_data = {
            'Attribute Name' : self.e1_attribute_name,
            'Data Type' : self.e1_data_type,
            'Key Constraint' : self.e1_constraint
        }
        self.e1_df = pd.DataFrame(e1_data, index= None)
        print("\nEntity 1 Attributes Defined:")
        print(self.e1_df)

    # Define entity 2 attributes
    def define_entity2(self, e2_attribute_name=[], e2_data_type=[], e2_constraint=[]):
        n_attribute = int(input("Enter the number of attributes in entity 2: "))
            
        # Ensure number of attributes is positive
        if n_attribute <= 0:
            print("The number of attributes must be greater than 0.")
            return
        
        # Collect attribute details for entity 2
        for i in range(n_attribute):
            print(f"\nEnter details for attribute {i + 1}:")
            attribute_name = input("Attribute Name: ").strip()
            data_type = input("Data Type (e.g., INT, VARCHAR): ").strip()
            constraint = input("Key Constraint (e.g., PK, FK, leave blank for none): ").strip().lower()
            
            # Append attribute details to lists
            self.e2_attribute_name.append(attribute_name)
            self.e2_data_type.append(data_type)
            self.e2_constraint.append(constraint or "None")

        # Create and display DataFrame for entity 2
        e2_data = {
            'Attribute Name' : self.e2_attribute_name,
            'Data Type' : self.e2_data_type,
            'Key Constraint' : self.e2_constraint
        }
        self.e2_df = pd.DataFrame(e2_data, index= None)
        print("\nEntity 2 Attributes Defined:")
        print(self.e2_df)

    # Build bridge table (many-to-many relationship) by checking PK and FK constraints
    def build_bride_table(self, r_attribute_name=[], r_data_type=[], r_constraint=[]):
        if ('pk' in self.e1_constraint and 'fk' in self.e2_constraint) or \
           ('pk' in self.e2_constraint and 'fk' in self.e1_constraint):

            # Append the PK and FK attributes to relationship attributes
            for i, constraint in enumerate(self.e1_constraint):
                if constraint in ['pk', 'fk']:
                    self.r_attribute_name.append(self.e1_attribute_name[i])
                    self.r_data_type.append(self.e1_data_type[i])
                    self.r_constraint.append(constraint)
            
            for i, constraint in enumerate(self.e2_constraint):
                if constraint in ['pk', 'fk']:
                    self.r_attribute_name.append(self.e2_attribute_name[i])
                    self.r_data_type.append(self.e2_data_type[i])
                    self.r_constraint.append(constraint)
            print('Bridge Table Successfully built.')
        else:
            print("Error: Unable to define relationship. Ensure PK and FK constraints are defined.")

    # Check if the entities follow First Normal Form (1NF)
    def check_normal_form_1(self):
        # 1NF: Ensures there is no repeating group of attributes (columns)
        if len(self.e1_attribute_name) == len(self.e1_data_type) and \
           len(self.e2_attribute_name) == len(self.e2_data_type):
            return True
        else:
            return False

    # Define 1:1 relation
    def relation_1_1(self):
        adjacency_matrix = [
            [0, 1],
            [1, 0]
        ]
        return adjacency_matrix

    # Define 1:N relation
    def relation_1_n(self, n):
        adjacency_matrix = [
            [0, 1],
            [n, 0]
        ]

        # Append the PK and FK attributes to many
        for i, constraint in enumerate(self.e1_constraint):
            if constraint in ['pk', 'fk']:
                self.e2_attribute_name.append(self.e1_attribute_name[i])
                self.e2_data_type.append(self.e1_data_type[i])
                self.e2_constraint.append(constraint)

        return adjacency_matrix

    # Define N:1 relation
    def relation_n_1(self, n):
        adjacency_matrix = [
            [0, n],
            [1, 0]
        ]

        # Append the PK and FK attributes to many
        for i, constraint in enumerate(self.e2_constraint):
            if constraint in ['pk', 'fk']:
                self.e1_attribute_name.append(self.e2_attribute_name[i])
                self.e1_data_type.append(self.e2_data_type[i])
                self.e1_constraint.append(constraint)

        return adjacency_matrix

    # Define N:M relation (many-to-many)
    def relation_n_m(self, n, m):
        self.build_bride_table()
        adjacency_matrix = [
            [0, 0, 1],
            [0, 0, n],
            [1, m, 0]
        ]
        return adjacency_matrix

    # Determine cardinality based on input values of n and m
    def cardinality(self):
        if self.n == 1 and self.m == 1:
            relation = self.relation_1_1()
        elif self.n == 1 and self.m != 1:
            relation = self.relation_1_n(self.m)
        elif self.n != 1 and self.m == 1:
            relation = self.relation_n_1(self.n)
        elif self.n != 1 and self.m != 1:
            relation = self.relation_n_m(self.n, self.m)
        return relation
    
    # Generate SQL CREATE statements for Entity 1 and Entity 2
    def generate_create_statements(self):
        # Generate CREATE statement for entity 1
        create_e1 = f"CREATE TABLE Entity1 (\n"
        for i in range(len(self.e1_attribute_name)):
            line = f"  {self.e1_attribute_name[i]} {self.e1_data_type[i].upper()}"
            if self.e1_constraint[i] != "None":
                line += f" {self.e1_constraint[i].upper()}"
            line += ",\n"
            create_e1 += line
        create_e1 = create_e1.rstrip(",\n") + "\n);"

        # Generate CREATE statement for entity 2
        create_e2 = f"CREATE TABLE Entity2 (\n"
        for i in range(len(self.e2_attribute_name)):
            line = f"  {self.e2_attribute_name[i]} {self.e2_data_type[i].upper()}"
            if self.e2_constraint[i] != "None":
                line += f" {self.e2_constraint[i].upper()}"
            line += ",\n"
            create_e2 += line
        create_e2 = create_e2.rstrip(",\n") + "\n);"

        return create_e1 , create_e2

    # Main method to interact with the user and build the schema
    def main(self):
        print("Define Entity 1:")
        self.define_entity1()
        print("\nDefine Entity 2:")
        self.define_entity2()

        # Check if entities are in 1NF
        if self.check_normal_form_1:
            print('It is in first normal form.')
        else:
            print('It is not in first normal form.')

        # Enter cardinality (relationship constraints)
        print("Enter Cardinality")
        self.n = int(input('Enter cardinality for entity1:'))
        self.m = int(input('Enter cardinality for entity2:'))
        self.schema_graph = self.cardinality()
        print('Set relation graph:')
        print(self.schema_graph)

        # Generate and print CREATE SQL statements
        create_e1, create_e2 = self.generate_create_statements()
        print("\nGenerated SQL Statements:")
        if self.n == 1 and self.m > 1:
            print(create_e2)
            print(create_e1)
        else:
            print(create_e1)
            print(create_e2)

        # Print the final database schema in graphical representation
        print('Database Schema:')
        if self.m > 1 and self.n > 1:
            print(f'{list(self.e1_attribute_name)}--1:{self.n}--{list(self.r_attribute_name)}--{self.m}:1--{list(self.e2_attribute_name)}')
        else:
            print(f'{list(self.e1_attribute_name)}--{self.n}:{self.m}--{list(self.e2_attribute_name)}')


# Run the main method
db_instance = database()
db_instance.main()

