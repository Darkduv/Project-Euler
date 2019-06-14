# %% Problem 301

# The first player loose if there is a 'nim sum', that is (a^b)^c == 0 where ^= XOR_bin
# so loose if n = "101...1000101..." in binary, with no one next. so no "..11.."

# we can see that nb(k) = F_k where nb(k) = nb of n of loose of len k in binary
# so nb_tot(n<= 2**k0)  = sum(F_k for k=1 to k0) + 1 (2**k0 is also a loose)
# that is nb_tot(n<= 2**k0)  = F_(k0+2) + 1
# with of course F_k = fibonacci_k with F_1 = F_2 = 1

phi = (1+5**0.5)/2
phi2 = 1/phi
n = 30
print(int(1/5**0.5*(phi**n - phi2**n)))
