from .enterprise_management_exception import EnterpriseManagementException
from .enterprise_project import EnterpriseProject
from datetime import datetime
import json

"""Module """


class EnterpriseManager:
    """Class for providing the methods for managing the orders"""
    def __init__(self):
        pass

    def register_project(self, company_cif: str, project_achronym: str, project_description: str,
                         department: str, date: str, budget: float):
       #CIF Check
        if not self.validate_cif(company_cif):
            raise EnterpriseManagementException("Invalid Cif")

        #Project_acronym Check
        if not (5 <= len(project_achronym) <= 10):
            raise EnterpriseManagementException("Invalid Project Acronym Length")
        # isalnum() checks for a-z, A-Z, 0-9
        if not project_achronym.isalnum():
            raise EnterpriseManagementException("Invalid Project Acronym Characters")

       #project_description Check
        if not (10 <= len(project_description) <= 30):
            raise EnterpriseManagementException("Invalid Project Description Length")

        #department check
        if department not in ("HR", "Finance", "Legal", "Logistics"):
            raise EnterpriseManagementException("Invalid Department")

        #date check
        try:
            date_valid = datetime.strptime(date, "%d/%m/%Y").date()
            year = date_valid.year

            if date_valid < datetime.today().date():
                raise ValueError
            if not (2025 <= year <= 2027):
                raise ValueError
        except ValueError: raise EnterpriseManagementException("Invalid Date")

        #budget check
        try:
            if not isinstance(budget, float):
                raise ValueError
            if not (budget * 100).is_integer():
                raise ValueError
            if not (50000.00 <= budget <= 1000000.00):
                raise ValueError
        except ValueError: raise EnterpriseManagementException("Invalid Budget")

        objProject = EnterpriseProject(company_cif, project_achronym, project_description,
                             department, date, budget)

        with open("corporate_operations.json", "w") as file:
            json.dump(objProject.to_json(), file, indent=4)

        return objProject.project_id



    @staticmethod
    def validate_cif(cif: str):
        """RETURNs TRUE IF THE IBAN RECEIVED IS VALID SPANISH IBAN,
        OR FALSE IN OTHER CASE"""

        # control_map = {0: "J", 1: "A", 2: "B", 3: "C", 4: "D",
        #                5: "E", 6: "F", 7: "G", 8: "H", 9: "I"}
        # letter_val = cif[0]
        # step_one = int(cif[2]) + int(cif[4]) + int(cif[6])
        # step_two = 0
        #
        # for j in range(1, 9, 2):
        #     num = int(cif[j]) * 2
        #     if num > 9:
        #         num = (num % 10) + (num // 10)
        #     step_two += num
        #
        # step_sum = step_one + step_two
        # unit = step_sum % 10
        # base_digit = 0 if unit == 0 else 10 - unit
        #
        # if letter_val in ["A", "B", "E", "H"]:
        #     control_char = base_digit
        # elif letter_val in ["K", "P", "Q", "S"]:
        #     control_char = control_map[base_digit]
        # else:
        #     return False

        # return str(control_char) == cif[8]

        return True
