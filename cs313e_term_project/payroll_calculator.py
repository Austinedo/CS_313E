"""
Modules for working with dataframes and .csv files
"""
import csv
from datetime import datetime
import pandas as pd


"""
Global constants
"""
STANDARD_WORK_WEEK_HRS = 40
OVERTIME_RATE = 1.5
HALF_RATE = 0.5
CSV_HEADER_PAYCHECK = ['Employee Name','Global Employee ID','Payroll ID','Pay Period','Base Wage(s)','Gross Pay','Total Hours','Overtime Hours','Regular Hours','Floor Hours','Closing Hours',
                       'Training Hours','Admin Hours','Reception Hours','Vacation Hours','Holiday Hours','Sick Hours', 'Overtime Hours Pay','Productivity Incentive','Product Incentive',
                       'New Return Incentive','Shift Incentive','All Other Incentives','Total Tips']
PAYCHECK_ATTR = ['_name', '_global_id', '_payroll_id', '_period', '_base_wage', '_gross_pay', '_total_hrs', '_overtime_hrs', 
                  '_regular_hrs', '_floor_hrs', '_closing_hrs', '_training_hrs', '_admin_hrs', '_reception_hrs', '_vacation_hrs', 
                  '_holiday_hrs', '_sick_hrs', '_overtime_hrs_pay', '_productivity_incent', '_product_incent', '_new_return_incent', 
                  '_shift_incent', '_all_other_incent', '_total_tips']

"""
Custom Exceptions
"""
class EmptyWeekListError(Exception):
    """
    custom exception for when there are no valid weeks found in the file
    """
    pass

def get_file_name(employee_dict: dict, payroll_type: str = ''):
    """
    Finds the range of weeks in 'employee_dict' and type of payroll csv file 
    and creates the name of the file
    """
    week_set = set()
    for employee in employee_dict.values():
        week_set.update(employee._weekly_paychecks.keys())
    
    week_list = sorted(week_set)
    
    if not week_list:
        raise EmptyWeekListError('WEEK LIST EMPTY: No valid weeks in this file')
    
    start_week = week_list[0].replace('/','-')
    end_week = week_list[-1].replace('/','-')

    return f'({start_week})-({end_week})_{payroll_type.capitalize()}Payroll.csv'

def correct_datetime(df):
    """
    corrects the date values if they occur in the format 'mm/dd/yyyy' to 'yyyy-mm-dd' 
    [this is to standardize all dates]
    """
    try:
        df['week ending'] = df['week ending'].apply(lambda x: datetime.strptime(x, "%m/%d/%Y").strftime("%Y-%m-%d"))
    except ValueError:
        pass

def PC_to_csv(employee_dict: dict, payroll_csv_type: str=''):
    """
    Writes paycheck information from each employee to appropriate .csv file type
    """
    with open(get_file_name(employee_dict, payroll_csv_type), mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(CSV_HEADER_PAYCHECK)
        rows = list()
        
        if payroll_csv_type.lower() == 'weekly':
            rows = [ [getattr(weekly_PC, attr) for attr in PAYCHECK_ATTR]
                     for employee in employee_dict.values() for weekly_PC in employee._weekly_paychecks.values()]
        elif payroll_csv_type.lower() == 'total':
            rows = [ [getattr(total_PC, attr) for attr in PAYCHECK_ATTR]
                      for employee in employee_dict.values() for total_PC in employee._total_paycheck.values()]
        writer.writerows(rows)


class Weekly_Paycheck:
    """
    Class that serves primarily as a data class that other 
    objects/functions/classes will operate on
    """
    def __init__(self, name, global_id, payroll_id, period, base_wage,
                 floor_hrs, closing_hrs, training_hrs, admin_hrs,
                 reception_hrs, vacation_hrs, holiday_hrs, sick_hrs,
                 productivity_incent, product_incent, new_return_incent,
                 shift_incent, all_other_incent, total_tips):
        # general paycheck information
        self._name = name
        self._global_id = global_id
        self._payroll_id = payroll_id
        self._base_wage = base_wage
        self._period = period
        self._floor_hrs = floor_hrs
        self._closing_hrs = closing_hrs
        self._training_hrs = training_hrs
        self._admin_hrs = admin_hrs
        self._reception_hrs = reception_hrs
        self._vacation_hrs = vacation_hrs
        self._holiday_hrs = holiday_hrs
        self._sick_hrs = sick_hrs
        self._productivity_incent = productivity_incent
        self._product_incent = product_incent
        self._new_return_incent = new_return_incent
        self._shift_incent = shift_incent
        self._all_other_incent = all_other_incent
        self._total_tips = total_tips
        # breakdown of hours and other info
        self._total_hrs = 0
        self._overtime_hrs = 0
        self._regular_hrs = 0
        self._total_bonuses = 0
        self._gross_pay = 0
        self._overtime_hrs_pay = 0

    def calculate_paycheck(self):
        """
        Calculates the correct pay for the weekly paycheck
        """
        self._total_hrs = (self._floor_hrs + self._closing_hrs + self._training_hrs +
                          self._admin_hrs + self._reception_hrs + self._vacation_hrs +
                          self._holiday_hrs + self._sick_hrs)
        self._total_bonuses = (self._productivity_incent + self._product_incent +
                               self._new_return_incent + self._shift_incent +
                               self._all_other_incent)

        if self._total_hrs > STANDARD_WORK_WEEK_HRS:
            self._overtime_hrs = self._total_hrs - STANDARD_WORK_WEEK_HRS
            self._regular_hrs = self._total_hrs - self._overtime_hrs - self._closing_hrs
            self._overtime_hrs_pay = self._base_wage * OVERTIME_RATE * self._overtime_hrs
            self._gross_pay = ((STANDARD_WORK_WEEK_HRS * self._base_wage) +
                               self._overtime_hrs_pay +
                               self._total_bonuses)
        else:
            self._regular_hrs = self._total_hrs - self._closing_hrs
            self._gross_pay = (self._total_hrs * self._base_wage) + self._total_bonuses


class Total_Paycheck(Weekly_Paycheck):
    """
    Inherits from Weekly_Paycheck Class and serves ONLY as a data 
    class that other objects/functions/classes will operate on
    """
    def __init__(self, name, global_id, payroll_id, period, 
                 base_wage, gross_pay, total_hrs, overtime_hrs, 
                 regular_hrs, floor_hrs, closing_hrs, training_hrs, 
                 admin_hrs, reception_hrs, vacation_hrs, holiday_hrs, 
                 sick_hrs, overtime_hrs_pay, productivity_incent, product_incent, 
                 new_return_incent, shift_incent, all_other_incent, total_tips):
        super().__init__(name, global_id, payroll_id, period, base_wage, floor_hrs, closing_hrs, 
                         training_hrs, admin_hrs, reception_hrs, vacation_hrs, holiday_hrs, sick_hrs, 
                         productivity_incent, product_incent, new_return_incent, shift_incent, 
                         all_other_incent, total_tips)
        self._total_hrs = total_hrs
        self._overtime_hrs = overtime_hrs
        self._regular_hrs = regular_hrs
        self._gross_pay = gross_pay
        self._overtime_hrs_pay = overtime_hrs_pay

class Employee:
    """
    Employee class that contains name, ID information, a dictionary
    of weekly paychecks, and a dictionary containing the total overall
    paycheck
    """
    def __init__(self, name, global_id, payroll_id):
        self._name = name
        self._global_id = global_id
        self._payroll_id = payroll_id
        self._weekly_paychecks = {}
        self._total_paycheck = {}

    def total_paycheck(self):
        """
        Finds the entire spanning pay period in the file and calculates the
        total pay and other info to the employee over the entire period
        """
        week_endings = sorted([ '(' + str(weeks) + ')' for weeks in self._weekly_paychecks.keys()])
        if week_endings:
            period = week_endings[0] + '-' + week_endings[-1]
        else:
            raise EmptyWeekListError('WEEK LIST EMPTY: No valid weeks in this file')
        
        # creates a dataframe of all the paychecks in the Employee() class self._weekly_pay and sums 
        # all information and creates a Total_Paycheck() class that contains the sum of all information
        paycheck_rows = [ [paycheck._name, paycheck._global_id, paycheck._payroll_id, paycheck._period, 
                           paycheck._base_wage, paycheck._gross_pay, paycheck._total_hrs, paycheck._overtime_hrs, 
                           paycheck._regular_hrs, paycheck._floor_hrs, paycheck._closing_hrs, paycheck._training_hrs, 
                           paycheck._admin_hrs, paycheck._reception_hrs, paycheck._vacation_hrs, paycheck._holiday_hrs, 
                           paycheck._sick_hrs, paycheck._overtime_hrs_pay, paycheck._productivity_incent,paycheck._product_incent,
                           paycheck._new_return_incent, paycheck._shift_incent, paycheck._all_other_incent, paycheck._total_tips]
                           for paycheck in self._weekly_paychecks.values() ]
        all_pc = pd.DataFrame(paycheck_rows, columns=[col.lower() for col in CSV_HEADER_PAYCHECK])
        self._total_paycheck[period] = Total_Paycheck(self._name, self._global_id, self._payroll_id, period, list(all_pc['base wage(s)'].unique()), all_pc['gross pay'].sum(), 
                                                      all_pc['total hours'].sum(), all_pc['overtime hours'].sum(), all_pc['regular hours'].sum(), all_pc['floor hours'].sum(), 
                                                      all_pc['closing hours'].sum(), all_pc['training hours'].sum(), all_pc['admin hours'].sum(), all_pc['reception hours'].sum(), 
                                                      all_pc['vacation hours'].sum(), all_pc['holiday hours'].sum(), all_pc['sick hours'].sum(),  all_pc['overtime hours pay'].sum(), 
                                                      all_pc['productivity incentive'].sum(), all_pc['product incentive'].sum(), all_pc['new return incentive'].sum(), 
                                                      all_pc['shift incentive'].sum(), all_pc['all other incentives'].sum(), all_pc['total tips'].sum())

    def employee_info(self):
        """
        Displays employee information and all paycheck information
        related to that employee
        """
        print('Name:', self._name)
        print('global ID:', self._global_id)
        print('payroll ID:', self._payroll_id)
        print('weeks pay:') # prints the dictionary of weekly paychecks
        for week, paycheck in self._weekly_paychecks.items():
            print(f'{week}: {paycheck._gross_pay:.2f} | {paycheck._gross_pay}')
        for key, value in self._total_paycheck.items():
            print(f'Period total {key}: {value._gross_pay:.2f} | {value._gross_pay}') # prints the dictionary of total paycheck
        print()

def main():
    """
    Main Function
    """
    # replace the file name with the desired file name HERE
    df = pd.read_csv('Payroll Consolidated 2023-08-04 - 2023-08-11.csv')
    df.columns = [col.lower() for col in df]

    # corrects the date values if they occur in the format 'mm/dd/yyyy' to 'yyyy-mm-dd' [this is to standardize all dates]
    correct_datetime(df)

    # Creates a dict. of unique employees found in the file and creates Employee class objects
    # that will contain all information regarding paychecks
    unique_employees = {employee_name: Employee(employee_name,
                                                df.loc[df['employee name'] == employee_name, 'global employee id'].values[0],
                                                df.loc[df['employee name'] == employee_name, 'payroll id'].values[0])
                        for employee_name in df['employee name'].unique()}
    
    # Filters and creates dataframes for each week's payroll
    weekly_payroll = [df[df['week ending'] == week].groupby(['employee name', 'week ending', 'global employee id', 'payroll id', 'base wage'], as_index=False).sum() 
                      for week in df['week ending'].unique() ]
    
    # Goes through weekly payroll df for each employee and appends paycheck if they worked that week
    for name, employee_info in unique_employees.items():
        for week in weekly_payroll:
            if name in week['employee name'].unique():
                period = week.loc[week['employee name'] == employee_info._name, 'week ending'].values[0]
                employee_info._weekly_paychecks[period] = Weekly_Paycheck(week.loc[week['employee name'] == employee_info._name, 'employee name'].values[0],
                                                                    week.loc[week['employee name'] == employee_info._name, 'global employee id'].values[0],
                                                                    week.loc[week['employee name'] == employee_info._name, 'payroll id'].values[0],
                                                                    week.loc[week['employee name'] == employee_info._name, 'week ending'].values[0],
                                                                    week.loc[week['employee name'] == employee_info._name, 'base wage'].values[0],
                                                                    week.loc[week['employee name'] == employee_info._name, 'floor hours'].values[0],
                                                                    week.loc[week['employee name'] == employee_info._name, 'closing hours'].values[0],
                                                                    week.loc[week['employee name'] == employee_info._name, 'training hours'].values[0],
                                                                    week.loc[week['employee name'] == employee_info._name, 'admin hours'].values[0],
                                                                    week.loc[week['employee name'] == employee_info._name, 'reception hours'].values[0],
                                                                    week.loc[week['employee name'] == employee_info._name, 'vacation hours'].values[0],
                                                                    week.loc[week['employee name'] == employee_info._name, 'holiday hours'].values[0],
                                                                    week.loc[week['employee name'] == employee_info._name, 'sick hours'].values[0],
                                                                    week.loc[week['employee name'] == employee_info._name, 'productivity incentive'].values[0],
                                                                    week.loc[week['employee name'] == employee_info._name, 'product incentive'].values[0],
                                                                    week.loc[week['employee name'] == employee_info._name, 'new return incentive'].values[0],
                                                                    week.loc[week['employee name'] == employee_info._name, 'shift incentive'].values[0],
                                                                    week.loc[week['employee name'] == employee_info._name, 'all other incentives'].values[0],
                                                                    week.loc[week['employee name'] == employee_info._name, 'total tips'].values[0])
                employee_info._weekly_paychecks[period].calculate_paycheck()
    
    # loops through all employees and calc. total paycheck over entire pay period and display
    for name, employee in unique_employees.items():
        employee.total_paycheck()
        employee.employee_info()

    # creates 2 .csv files for weekly paychecks and total paychecks
    PC_to_csv(unique_employees, 'weekly')
    PC_to_csv(unique_employees, 'total')

if __name__ == '__main__':
    main()