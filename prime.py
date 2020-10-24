def isPrime(n): 
    if (n == 1): 
        return False 
    for i in range(2, n): 
        if (n % i == 0): 
            return False
    return True
    
if isPrime(11): 
    print ("true") 
else: 
    print ("false") 
fun getMoneySpent(keyboards: Array<Int>, drives: Array<Int>, b: Int): Int {
    var countItem = -1
    for(k in keyboards.indices){

        for(d in drives.indices){
            val total = keyboards[k] + drives[d]
            if(total <= b && countItem < total){
                countItem = total
