# Ten program pokazuje, jak liczba zmiennoprzecinkowa
# może zostać sformatowana jako wartość pieniężna.
monthly_pay = 5000.0
annual_pay = monthly_pay * 12
print('Opłata roczna wynosi',
      format(annual_pay, ',.2f'),
      'zł.', sep='')
