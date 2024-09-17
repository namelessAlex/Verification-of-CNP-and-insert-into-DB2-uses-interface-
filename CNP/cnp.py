class CNP:
    # initialize the CNP class
    def __init__(self, cnp):
        self.cnp = cnp
        self.century = None
        self.gender = None  
        self.month = None
        self.day = None
        self.county = None
        self.first_char = None

    # check the length of the CNP. it has to be a specific length of 13
    def check_length(self):
        
         if len(self.cnp) != 13:
            raise InvalidCNPError(f'Length of CNP not ok: length of {len(self.cnp)}', code = 1001)
    
    #check the first char from the CNP
    def check_sex(self):
        first_char = int(self.cnp[0])
        self.first_char = first_char
        gender_list = ['masculin','feminin']
        
        if first_char in (1,3,5):
                return gender_list[0]
        elif first_char in (2,4,6):
                return gender_list[1]
        else:
            raise InvalidCNPError(print(f'def validare_sex error, first char not in range(1 thru 6): {first_char}'), code = 1002 )    
    
    #check the century based on the first char of the CNP
    def check_century(self):
        century_list = ['18','19','20']
        if self.first_char in (1,2):
            self.century = century_list[self.first_char]
        elif self.first_char in (3,4):
            self.century = century_list[self.first_char]
        elif self.first_char in (5,6):
            self.century = century_list[self.first_char]   

    #get the century of birth(18, 19 or 20)     
    def get_century(self):
        if self.century:
            return self.century
        else:
            raise InvalidCNPError(print(f'Century unknown: {self.century}'), code = 1003 )        
    
    #get the year of birth
    def get_year(self):    
        year = self.cnp[1] + self.cnp[2]
        return year
    
    #get the month of birth
    def get_month(self):  
        self.month = self.cnp[3] + self.cnp[4]
        return self.month
    
    #get the day of birth
    def get_day(self):             
        day = self.cnp[5] + self.cnp[6]
        self.day = int(day)
        if self.day in range(1,32):
            return day
        else:
            raise InvalidCNPError(print(f'def get_day error: {self.day}'), code = 1004 )
    
    #get the county of birth
    def get_county(self):
        self.county = self.cnp[7] + self.cnp[8]
        county = int(self.county)
        return county
    
    #check the month of birth to be displayed
    def check_month(self):
        month_list = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
        ]
        month_nr = int(self.month)
        if month_nr in (1,3,5,7,8,10,12):
            if self.day in range(1,32):
                return month_list[month_nr-1]
            else:
                raise InvalidCNPError(print(f'def check month error, day not in range for month {month_nr}: {self.day}'), code = 1005 )   
        elif month_nr == 2:
            if self.day in range(1,29):
                return month_list[month_nr-1]
            else:
                raise InvalidCNPError(print(f'def check month error, day not in range for month {month_nr}: {self.day}'), code = 1006 )   
        elif month_nr in (4,6,9,11):
            if self.day in range(1,31):
                return month_list[month_nr-1]
            else:
                raise InvalidCNPError(print(f'def check month error, day not in range for month {month_nr}: {self.day}'), code = 1007 )   
        else:
            raise InvalidCNPError(print(f'def check month error, day not in range for month {month_nr}: {self.day}'), code = 1008 )    
    
    #check the county of birth
    def check_county(self):
        cnp_county_codes = {
    "01": "Alba", "02": "Arad", "03": "Argeș", "04": "Bacău", "05": "Bihor", "06": "Bistrița-Năsăud",
    "07": "Botoșani", "08": "Brașov", "09": "Brăila", "10": "Buzău", "11": "Caraș-Severin", "12": "Cluj",
    "13": "Constanța", "14": "Covasna", "15": "Dâmbovița", "16": "Dolj", "17": "Galați", "18": "Gorj",
    "19": "Harghita", "20": "Hunedoara", "21": "Ialomița", "22": "Iași", "23": "Ilfov", "24": "Maramureș",
    "25": "Mehedinți", "26": "Mureș", "27": "Neamț", "28": "Olt", "29": "Prahova", "30": "Satu Mare",
    "31": "Sălaj", "32": "Sibiu", "33": "Suceava", "34": "Teleorman", "35": "Timiș", "36": "Tulcea",
    "37": "Vaslui", "38": "Vâlcea", "39": "Vrancea", "40": "Bucharest", "41": "Bucharest, Sector 1",
    "42": "Bucharest, Sector 2", "43": "Bucharest, Sector 3", "44": "Bucharest, Sector 4",
    "45": "Bucharest, Sector 5", "46": "Bucharest, Sector 6", "51": "Călărași", "52": "Giurgiu"
                            }
        if self.county in cnp_county_codes:
            county = cnp_county_codes[self.county]
            return county
        else:
            raise InvalidCNPError(print(f'County code incorrect: {cnp_county_codes[self.county]}'), code = 1009)
    
    #check the sequential number between 001 - 999
    def check_sequential_number(self):
        s = int(self.cnp[0])
        sequential_number = int(self.cnp[9:12])
        if sequential_number < 1 or sequential_number > 999:
            raise InvalidCNPError(print(f'sequential_number unknown: {sequential_number}') )              
        if (s in [1, 3, 5, 7] and sequential_number >= 500) or (s in [2, 4, 6, 8] and sequential_number < 500):
            raise InvalidCNPError("Invalid sequential_number: Inconsistent with gender.")
    
    #check the control digit
    def check_control_digit(self):
    # Weights for the control digit calculation
        weights = [2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9]
    # Extract the first 12 digits and the control digit    
        digits = [int(self.cnp[i]) for i in range(12)]
        control_digit = int(self.cnp[12])
    # Calculate the sum of products of weights and corresponding digits
        total_sum = sum(weights[i] * digits[i] for i in range(12))
    # Calculate the remainder
        remainder = total_sum % 11
    # Determine the expected control digit
        expected_control_digit = 1 if remainder == 10 else remainder
    # Compare with the provided control digit
        if control_digit == expected_control_digit:
            return 
        else:
            raise InvalidCNPError(print(f'return digit invalid: {control_digit}'), code = 1010 )    

class Persoana(CNP):
    def __init__(self, cnp, nume, prenume):
        super().__init__(cnp)
        self.nume = nume
        self.prenume = prenume
    
    def afiseaza_informatii(self):
        return f"Nume: {self.nume}, Prenume: {self.prenume}, CNP: {self.cnp}"

class Angajat(Persoana):
    def __init__(self, cnp, nume, prenume, pozitie):
        super().__init__(cnp, nume, prenume)
        self.pozitie = pozitie
    
    def afiseaza_detalii_angajat(self):
        return f"{self.afiseaza_informatii()}, Pozitie: {self.pozitie}"

class InvalidCNPError(Exception):
    def __init__(self, message="Invalid CNP provided", code = None):
        super().__init__(message)
        self.code = code
        self.message = message

    def __str__(self):
        return f"{self.__class__.__name__}: {self.message}"
    
class MainFunction():
    def show_details_for_person(person):
        try:
            cnp_person = CNP(person.cnp)
            cnp_person.check_length()  # Validate length of CNP
            cnp_person.check_sequential_number()
            # Additional checks and information extraction
            sex = cnp_person.check_sex()
            day = cnp_person.get_day()
            month = cnp_person.get_month()
            year = cnp_person.get_year()
            cnp_person.check_century()
            century = cnp_person.get_century()
            year = century + year
            luna = cnp_person.check_month()
            cnp_person.get_county()
            county = cnp_person.check_county()

            cnp_person.check_control_digit()

            # Return formatted details if all checks pass
            return f'''
{person.nume} {person.prenume}, de sex {sex}, 
nascut la data de: ziua {day}, luna {luna}, anul {year}
in judetul {county}
            '''

        except InvalidCNPError as e:
            # Check the code and display appropriate error message
            if e.code == 1001:
                return f"Error: Length of CNP is not correct. {e}"
            elif e.code == 1002:
                return f"Error: Invalid gender code. {e}"
            elif e.code == 1003:
                return f"Error: Unknown century. {e}"
            elif e.code == 1004:
                return f"Error: Invalid day. {e}"
            elif e.code == 1005:
                return f"Error: Day not valid for the given month. {e}"
            elif e.code == 1006:
                return f"Error: Day not valid for February. {e}"
            elif e.code == 1007:
                return f"Error: Day not valid for the month with 30 days. {e}"
            elif e.code == 1008:
                return f"Error: Invalid month. {e}"
            elif e.code == 1009:
                return f"Error: Invalid county code. {e}"
            elif e.code == 1010:
                return f"Error: Invalid sequential number. {e}"
            elif e.code == 1011:
                return f"Error: Sequential number out of range. {e}"
            elif e.code == 1012:
                return f"Error: Sequential number inconsistent with gender. {e}"
            elif e.code == 1013:
                return f"Error: Invalid control digit. {e}"
            else:
                return f"Error: An unknown error occurred. {e}"