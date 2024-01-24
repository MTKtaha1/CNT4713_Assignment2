import socket
class Assignment2:

    def __init__(self, year):
        self.year = year
    
    def tellAge(self, currentYear):
        birthyear = currentYear - self.year
        print(f"Your age is {birthyear}")

    def listAnniversaries(self):
        current_year =2022
        anniversary = [i for i in range(10, current_year - self.year + 1, 10)]
        return anniversary
    def modifyYear(self, n):
        year_str = str(self.year)

        # Extract the first two characters of the year
        first_two_chars = year_str[:2]

        # Extract odd positioned characters of the year
        odd_chars = year_str[::2]
        
        modified_string = first_two_chars * n + odd_chars * n

        return modified_string
    
    @staticmethod
    def checkGoodString(string):
        if len(string) < 9:
            return False

    # Checking password starts with a lower case letter a-z
        if not string[0].islower() or not string[0].isalpha():
            return False

    # Checking password contains only one number
        if sum(c.isdigit() for c in string) != 1:
            return False

        return True
    
    
    
    @staticmethod
    def connectTcp(host, port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((host, port))
            return True
        except Exception as e:
            return False


