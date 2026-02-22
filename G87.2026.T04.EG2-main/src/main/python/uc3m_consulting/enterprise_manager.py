from .enterprise_management_exception import EnterpriseManagementException
from .enterprise_project import EnterpriseProject
from datetime import datetime

"""Module """

class EnterpriseManager:
    """Class for providing the methods for managing the orders"""
    def __init__(self):
        pass

    def register_project(self, company_cif: str, project_acronym: str, project_description: str,
                         department: str, date: str, budget: float):
        if not self.validate_cif():
            raise EnterpriseManagementException("Invalid Cif")

        if len(project_acronym) > 10 or len(project_acronym) < 5:
            raise EnterpriseManagementException("Invalid Project Acronym Length")
        if not project_acronym.isalnum:
            raise EnterpriseManagementException("Invalid Project Acronym Characters")

        if not len(project_description) <= 30 or len(project_description) >= 10:
            raise EnterpriseManagementException("Invalid Project Description Length")

        try:
            datetime.strptime(date, "%d/%m/%Y").date()
        except ValueError: raise EnterpriseManagementException("Invalid Date")
        if date < datetime.date.today():
            raise EnterpriseManagementException("Invalid Date")

        if budget < 50000:
            raise EnterpriseManagementException("Budget too low")
        objProject = enterprise_project(company_cif, project_acronym, project_description,
                             department, date, budget)
        return objProject.project_id



    @staticmethod
    def validate_cif(cif: str):
        """RETURNs TRUE IF THE IBAN RECEIVED IS VALID SPANISH IBAN,
        OR FALSE IN OTHER CASE"""
        return True
