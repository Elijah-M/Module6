"""
Author: Elijah Morishita
elmorishita@dmacc.edu
9/30/3030
An Inner Functions Program that gather area and perimeter info
"""

def measurements(length, width):
    """
    This function takes length and width measurements, and prints the area and perimeter results
    :param length:
    :param width:
    :return: results
    """

    len_wid = [length, width]

    def area(len_wid):
        """
        This function calculates area
        :param len_wid:
        :return: area
        """
        area = str(float(len_wid[0] * len_wid[1]))

        return area

    def perimeter(len_wid):
        """
        This function calculates perimeter
        :param len_wid:
        :return: perimeter
        """

        perimeter = str(float(len_wid[0] * 2 + (len_wid[1] * 2)))

        return perimeter

    # Combine the results of the area() and perimeter() functions into 1 string
    results = "Perimeter = " + perimeter(len_wid) + " Area = " + area(len_wid)
    return results

if __name__ == '__main__':
    print(measurements(3, 4))