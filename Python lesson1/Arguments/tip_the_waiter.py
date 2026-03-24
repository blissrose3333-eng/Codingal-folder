def total_calu(bill_amount,tip_perc):
    total=bill_amount*(1+ 0.01*tip_perc)
    total=round(total,2)
    print(f"Please pay ${total}")

total_calu(150,20)