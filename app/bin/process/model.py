import csv
from datetime import datetime


class Process:

    def __init__(self, app):
        self.app = app

    def process_nested_list(self, nested_list, result_list):
        """ Process a nested list
            Parameters:
            argument1 (list): nested list

            Returns:
            Only one list

        """
        for item in nested_list:
            if isinstance(item, list):
                self.process_nested_list(item, result_list)
            else:
                result_list.append(item)

        self.save_result_list(result_list)

        return result_list

    @staticmethod
    def save_result_list(result_list):
        """ Save List Result in CSV file
            Parameters:
            argument1 (list): list to save
        """
        today = datetime.today()
        year, month, day, hour = today.year, today.month, today.day, today.hour
        file_name = 'reports/result.{}{}{}{}.csv'.format(year, month, day, hour)

        with open(file_name, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(result_list)
