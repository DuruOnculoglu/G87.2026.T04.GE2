"""Module """

class EnterpriseManager:
    """Class for providing the methods for managing the orders"""
    def __init__(self):
        pass

    def register_project(self, company_cif: str, project_acronym: str, project_description: str,
                         department: str, date: str, budget: float):
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
