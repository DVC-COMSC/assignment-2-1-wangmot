def main():
    """
    ##################################################
    Comlete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """
    males = input("how many males: ")
    females = input("how many females: ")

    total_num = int(males) + int(females)
    
    m_perc = (int(males)/total_num)*100
    #m_perc/100
    f_perc = (int(females)/total_num)*100
    #f_perc/100

    print('The total number of students is ', total_num)
    print('The total number of males and females: ', males, females)
    #print(f_perc)
    print(f'The percentage of males and females \t {m_perc: .2f} {f_perc: .2f}')


    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc


if __name__ == '__main__':
    main()
