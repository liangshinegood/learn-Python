# Ë¼Â·£º1. ¸ù¾İÄêÁäÅÅĞò£»2.¸ÏàÍ¬ÄêÁä¸ù¾İÊäÈëµÄË³ĞòÅÅĞò£»3.Èç¹ûÊÇM ¸ñÊ½ÎªMr.
# Èç¹ûÊÇF ¸ñÊ½ÎªMs.

def person_lister(f):
    def inner(people):
        return map(f,sorted(people,key=lambda x:x[2]))
    return inner




