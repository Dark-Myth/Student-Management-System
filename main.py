"""Student Management System"""

print(" _______________________________________________________________________________________________________")
print("\t\t\t\t\t\t\t\t\tSTUDENT MANAGEMENT SYSTEM\t\t\t\t\t\t\t\t\t\t\t")
print(" -------------------------------------------------------------------------------------------------------")


def menu():
    print("[---------------MENU---------------]")
    print("\t1.\tAdd Student Details:")
    print("\t2.\tSearch Student Details:")
    print("\t3.\tDisplay Student:")
    print("\t4.\tDelete Student Details:")
    print("\t5.\tExit:")
    print("----------------------------------")
    choice = int(input("Enter your choice: "))
    print(" ---------------------------------")
    return choice


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.id = data[0]
        self.name = data[1]
        self.dept = data[2]
        self.course = data[3]
        self.cgpa=data[4]


'''Creation of a BST with student details'''

def copy(root,key):
    root.name = key[1]
    root.dept = key[2]
    root.course = key[3]
    root.cgpa = key[4]
    return root
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.id == key[0]:
            print("The Entry is already found:")
            if(input("Would you like to update the record: 1(yes)/(no)otherwise"
                     "->")=='1'):
                print("The Old Student Record is Updated!!!")
                return copy(root, key)
            else:
                return root

        elif root.id < key[0]:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root


def storeBSTNodes(root, nodes):
    if not root:
        return
    storeBSTNodes(root.left, nodes)
    nodes.append(root)
    storeBSTNodes(root.right, nodes)


def buildTreeUtil(nodes, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    node = nodes[mid]
    node.left = buildTreeUtil(nodes, start, mid - 1)
    node.right = buildTreeUtil(nodes, mid + 1, end)
    return node


def buildTree(root):
    nodes = []
    storeBSTNodes(root, nodes)
    n = len(nodes)
    return buildTreeUtil(nodes, 0, n - 1)


'''The following functions are used to search for the student details'''


def search(root, id):
    if root is None or root.id == id:
        return root
    if root.id < id:
        return search(root.right, id)
    return search(root.left, id)


'''The following functions are used to print the student details in user specified manner'''


def inorder(root):
    if root:
        inorder(root.left)
        print(f"{root.id}   \t\t\t  {root.name} \t\t\t  {root.dept} \t\t\t  {root.course}   \t\t\t  {root.cgpa}")
        inorder(root.right)


def display_dept(root, dept):
    if root:
        display_dept(root.left, dept)
        if root.dept == dept:
                print(f"{root.id}   \t\t\t  {root.name} \t\t\t  {root.dept} \t\t\t  {root.course}   \t\t\t  {root.cgpa}")
        display_dept(root.right, dept)


def display_course(root, course):
    if root:
        display_course(root.left, course)
        if root.course == course:
                print(f"{root.id}   \t\t\t  {root.name} \t\t\t  {root.dept} \t\t\t  {root.course}   \t\t\t  {root.cgpa}")
        display_course(root.right, course)

def preorder(root):
        if root:
            print(f"{root.id}   \t\t\t  {root.name} \t\t\t  {root.dept} \t\t\t  {root.course}   \t\t\t  {root.cgpa}")
            inorder(root.left)
            inorder(root.right)


'''The following functions are used to delete the student details'''


def deleteNode(root, id):
    if root is None:
        return root
    if root.id > id:
        root.id = deleteNode(root.left, id)
        return root
    elif root.id < id:
        root.right = deleteNode(root.right, id)
        return root

    if root.left is None:
        temp = root.right
        del root
        return temp
    elif root.right is None:
        temp = root.left
        del root
        return temp


    else:
        succParent = root
        succ = root.right
        while succ.left is not None:
            succParent = succ
            succ = succ.left
        if succParent != root:
            succParent.left = succ.right
        else:
            succParent.right = succ.right
        root.id = succ.id
        root.name = succ.name
        root.dept = succ.dept
        root.course = succ.course
        root.cgpa = succ.cgpa
        del succ
        return root


if __name__ == '__main__':
    choice=100
    student_no=0
    while(choice != 5):

        if(student_no%10==0 and student_no>1):
            buildTree(database)
            print("The Tree was restructured to improve efficiency!!!")

        print()
        choice = menu()
        print()
        if(choice == 1):
            print("                        ADDING...")
            student=[]
            student.append(int(input("Roll Number:")))
            student.append(input("Name:"))
            student.append(input("Department:"))
            student.append(input("Course:"))
            student.append(float(input("CGPA:")))
            if(student_no==0):
                database=Node(student)
            else:
                database=insert(database,student)
            student_no+=1




        elif (choice==2):
            print("                        SEARCHING")
            if(student_no!=0):
                id = int(input("Enter the Student Id(to be searched):"))
                root=search(database, id)
                if(root==None):
                    print("Student Detail not Found!!!.")
                else:
                    print(
                        f"{root.id}   \t\t\t  {root.name} \t\t\t  {root.dept} \t\t\t  {root.course}   \t\t\t  {root.cgpa}")
            else:
                print("The Database is Empty.......")


        elif( choice==3):
            print("                        DISPLAY")
            if(student_no!=0):
                print("Note:- if above choice not selected all would be printed")
                print("1. Department")
                print("2. Course")
                display = (input("->"))
                print()
                if (display == '1'):
                    dept = input("Enter Department:")
                    print(dept)
                    print("Roll Number       Name                Department         Course              CGPA")
                    display_dept(database, dept)
                    print("     -              -                     -                 -                  -")
                elif display == '2':
                    course = input("Enter Course:")
                    print(course)
                    print("Roll Number       Name                Department         Course              CGPA")
                    display_course(database, course)
                    print("     -              -                     -                 -                  -")
                else:
                    print("DATABASE")
                    print("Roll Number       Name                Department         Course              CGPA")
                    inorder(database)
            else:
                print("The Database is Empty.......")


        elif(choice == 4):
            print("                        DELETING")
            if(student_no!=0):
                id=int(input("Enter Student Id(to be deleted):"))
                if(search(database,id) is None):
                    print("Student with Id:",id,"not found!!!")
                else:
                    database = deleteNode(database,id)
                    print("Student with Id:",id,"deleted!!!")
                    student_no -= 1
            else:
                print("The Database is Empty.......")


        elif(choice==5):
            print("END OF PROGRAM")

        else:
            print("Enter Valid Input!!!")




