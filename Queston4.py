class py_solution:
   def is_valid_parenthese(self, str1)->bool:
        stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
        for parenthese in str1:
            if parenthese in pchar.keys():
                stack.append(parenthese)
            else:
                if stack == []:
                    return False
                a = stack.pop()
                if parenthese!= pchar[a]:
                    return False
        return len(stack)==0
sol=py_solution()
str1="(){}[]"
str2="()[{)}"
str3="()"
print(str1,sol.is_valid_parenthese(str1))
print(str2,sol.is_valid_parenthese(str2))
print(str3,sol.is_valid_parenthese(str3))

