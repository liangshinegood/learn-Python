# Ë¼Â·£ºÓÃset ·½·¨ÖĞµÄintersectionÕÒ³ö²»Í¬
# ½«Á½ÖÖ²»Í¬µÄÖµºÏ²¢Ò»ÏÂ£¬×îºó´ğÓ¦´³öÀ´

a,b = [set(input().split()) for _ in range(4)][1::2]
print(*sorted(a^b,key=int),sep='\n')


