#User function Template for python3
class Solution:
    def isValid(self, s):
        #code here
        stripped = s.split('.')
        if len(stripped) != 4 or '' in stripped:
            return False
        else:
            for i in stripped:
                if not ( 0<=int(i)<= 255) or (i[0] == "0" and len(i) > 1):
                    return False
            return True
        

#Back-end complete function Template for Python 3


class Solution:
    # Function to validate an IP address
    def isValid(self, s):
        counter = 0
        for i in range(0, len(s)):
            # Count the number of periods (.)
            if (s[i] == '.'):
                counter = counter + 1
        # If the number of periods is not 3, IP address is invalid
        if (counter != 3):
            return 0

        # Create a set to store all possible values of a byte (0-255)
        st = set()
        for i in range(0, 256):
            st.add(str(i))

        counter = 0
        temp = ""
        for i in range(0, len(s)):
            # If character is not a period (.), add it to the temporary string
            if (s[i] != '.'):
                temp = temp + s[i]
            else:
                # Check if the temporary string is a valid byte
                if (temp in st):
                    counter = counter + 1
                temp = ""
        # Check if the final temporary string is a valid byte
        if (temp in st):
            counter = counter + 1

        # If the number of valid bytes is 4, IP address is valid
        if (counter == 4):
            return 1
        else:
            return 0