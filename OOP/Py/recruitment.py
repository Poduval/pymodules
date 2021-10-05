"""
Example of creating classes using object oriented programming
"""

# Initialize python modules
import re
import pandas as pd

# Defining recruitment class
class Recruitment():
    """
    Analyse recruitment data with pre-defined structure
    """
    # class attribute
    expected_fields = ['name', 'sex', 'college', 'grade', 'HRScore', 'reportingScore',
                       'technicalScore', 'theoreticalScore']
    score_fields = [i for i in expected_fields if re.findall(r'Score', i)]
    output_fields = ['college', 'name', 'finalScore']
    n_score_fields = 4

    # instance attribute
    def __init__(self, df: pd.DataFrame):
        """
        Initialize the class
        :param df: input pandas dataframe
        """
        self.df = df.copy()
        self.n_candidates = len(self.df)
        check = all([i in self.df.columns for i in self.expected_fields])
        if check:
            print("Input is validated, Number of candidates --> ", self.n_candidates)
            self.df['finalScore'] = self.df[self.score_fields].sum(axis=1) / self.n_score_fields
        else:
            return print("Input format is not proper, Expecting the following mandatory fields: ",
                         self.expected_fields)

    def Attributes(self):
        return['df', 'n_candidates', 'Overview', 'Results']

    def Overview(self):
        """
        :return: Overall count per college and sex
        """
        # print(self.Attributes())
        return self.df.groupby(by=['sex', 'college']).size()

    def Results(self, n=3, top=True):
        """
        Get final list of candidates
        :param n: number of candidates
        :param top: True (best)/False (Worst)
        :return: final list of candidates
        """
        n = min(n, self.n_candidates)
        return self.df.sort_values(ascending=not top, by='finalScore')[self.output_fields].head(n)
