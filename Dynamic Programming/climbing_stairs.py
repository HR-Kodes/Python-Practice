def climbing(n) :
    if (n==0 or n==1) : return 1
    left = climbing (n-1)
