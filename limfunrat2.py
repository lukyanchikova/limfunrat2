def limzero(a1,b1,c1,a2,b2,c2):
    
    import math

    if a2!=0 or b2!=0 or c2!=0:        
        x=[]
        y=[]
        z=[]
        if a2!=0:
            if b2**2-4*a2*c2>=0:
                z.append((math.sqrt(b2**2-4*a2*c2)-b2)/(2*a2))
                z.append((-math.sqrt(b2**2-4*a2*c2)-b2)/(2*a2))
            for i in range(-101,100):
                x.append((i+1)/100)
                if len(z)>0:
                    if x[i+101] not in z:
                        y.append((a1*x[i+101]**2+b1*x[i+101]+c1)/(a2*x[i+101]**2+b2*x[i+101]+c2))
                    else:
                        y.append(None)
                else:
                    y.append((a1*x[i+101]**2+b1*x[i+101]+c1)/(a2*x[i+101]**2+b2*x[i+101]+c2))
        else:
            if b2!=0:
                z.append(-c2/b2)
            for i in range(-101,100):
                x.append((i+1)/100)
                if len(z)>0:
                    if x[i+101] not in z:
                        y.append((a1*x[i+101]**2+b1*x[i+101]+c1)/(a2*x[i+101]**2+b2*x[i+101]+c2))
                    else:
                        y.append(None)
                else:
                    y.append((a1*x[i+101]**2+b1*x[i+101]+c1)/(a2*x[i+101]**2+b2*x[i+101]+c2))

        import matplotlib.pyplot as plt

        if c1!=0 and c2!=0:
            plt.plot(x,y)
            plt.axhline(y = c1/c2, linestyle = '-.')
            if len(z)>0:
                for i in range(len(z)):
                    plt.axvline(x = z[i], linestyle = '-.')
            plt.show()
            return (c1/c2,c1/c2,z)
        if c1==0 and c2!=0:
            plt.plot(x,y)
            plt.axhline(y = 0, linestyle = '-.')
            if len(z)>0:
                for i in range(len(z)):
                    plt.axvline(x = z[i], linestyle = '-.')
            plt.show()
            return (0,0,z)
        if c1!=0 and c2==0:
            if c1*b2>0:
                plt.plot(x,y)
                if len(z)>0:
                    for i in range(len(z)):
                        plt.axvline(x = z[i], linestyle = '-.')
                plt.show()
                return ("Inf","-Inf",z)
            elif c1*b2==0 and c1*a2>0:
                plt.plot(x,y)
                if len(z)>0:
                    for i in range(len(z)):
                        plt.axvline(x = z[i], linestyle = '-.')
                plt.show()
                return ("Inf","-Inf",z)
            else:
                plt.plot(x,y)
                if len(z)>0:
                    for i in range(len(z)):
                        plt.axvline(x = z[i], linestyle = '-.')
                plt.show()
                return ("-Inf","Inf",z)
        if c1==0 and c2==0:
            if b1!=0 and b2!=0:
                plt.plot(x,y)
                if len(z)>0:
                    for i in range(len(z)):
                        plt.axvline(x = z[i], linestyle = '-.')
                plt.axhline(y = b1/b2, linestyle = '-.')
                plt.show()
                return (b1/b2,b1/b2,z)
            if b1==0 and b2!=0:
                plt.plot(x,y)
                if len(z)>0:
                    for i in range(len(z)):
                        plt.axvline(x = z[i], linestyle = '-.')
                plt.axhline(y = 0, linestyle = '-.')
                plt.show()
                return (0,0,z)
            if b1!=0 and b2==0:
                if b1*a2>0:
                    plt.plot(x,y)
                    if len(z)>0:
                        for i in range(len(z)):
                            plt.axvline(x = z[i], linestyle = '-.')
                    plt.show()
                    return ("Inf","-Inf",z)
                elif b1*a2==0:
                    plt.plot(x,y)
                    if len(z)>0:
                        for i in range(len(z)):
                            plt.axvline(x = z[i], linestyle = '-.')
                    plt.show()
                    return ("Inf","-Inf",z)    
                else:
                    plt.plot(x,y)
                    if len(z)>0:
                        for i in range(len(z)):
                            plt.axvline(x = z[i], linestyle = '-.')
                    plt.show()
                    return ("-Inf","Inf",z)
            if b1==0 and b2==0:
                if a1!=0 and a2!=0:
                    plt.plot(x,y)
                    if len(z)>0:
                        for i in range(len(z)):
                            plt.axvline(x = z[i], linestyle = '-.')
                    plt.axhline(y = a1/a2, linestyle = '-.')
                    plt.show()
                    return (a1/a2,a1/a2,z)
                if a1==0 and a2!=0:
                    plt.plot(x,y)
                    if len(z)>0:
                        for i in range(len(z)):
                            plt.axvline(x = z[i], linestyle = '-.')
                    plt.axhline(y = 0, linestyle = '-.')
                    plt.show()
                    return (0,0,z)
                if a1!=0 and a2==0:
                    return 'Err'
                if a1==0 and a2==0:
                    return 'Err'
    else:
        return 'Err'

def liminf(a1,b1,c1,a2,b2,c2):
    
    import math
    
    if a2!=0 or b2!=0 or c2!=0:        
        x=[]
        y=[]
        z=[]
        if a2!=0:
            if b2**2-4*a2*c2>=0:
                z.append((math.sqrt(b2**2-4*a2*c2)-b2)/(2*a2))
                z.append((-math.sqrt(b2**2-4*a2*c2)-b2)/(2*a2))
            for i in range(-101,100):
                x.append((i+1)/1)
                if len(z)>0:
                    if x[i+101] not in z:
                        y.append((a1*x[i+101]**2+b1*x[i+101]+c1)/(a2*x[i+101]**2+b2*x[i+101]+c2))
                    else:
                        y.append(None)
                else:
                    y.append((a1*x[i+101]**2+b1*x[i+101]+c1)/(a2*x[i+101]**2+b2*x[i+101]+c2))
        else:
            if b2!=0:
                z.append(-c2/b2)
            for i in range(-101,100):
                x.append((i+1)/1)
                if len(z)>0:
                    if x[i+101] not in z:
                        y.append((a1*x[i+101]**2+b1*x[i+101]+c1)/(a2*x[i+101]**2+b2*x[i+101]+c2))
                    else:
                        y.append(None)
                else:
                    y.append((a1*x[i+101]**2+b1*x[i+101]+c1)/(a2*x[i+101]**2+b2*x[i+101]+c2))

        import matplotlib.pyplot as plt

        if a1==0 and a2!=0:
            plt.plot(x,y)
            if len(z)>0:
                for i in range(len(z)):
                    plt.axvline(x = z[i], linestyle = '-.')
            plt.axhline(y = 0, linestyle = '-.')
            plt.show()
            return (0,0,z)
        if a1!=0 and a2==0:
            if a1*b2>0:
                plt.plot(x,y)
                if len(z)>0:
                    for i in range(len(z)):
                        plt.axvline(x = z[i], linestyle = '-.')
                plt.show()
                return ('Inf','-Inf',z)
            elif a1*b2==0 and a1*c2>0:
                plt.plot(x,y)
                if len(z)>0:
                    for i in range(len(z)):
                        plt.axvline(x = z[i], linestyle = '-.')
                plt.show()
                return ('Inf','-Inf',z)
            else:
                plt.plot(x,y)
                if len(z)>0:
                    for i in range(len(z)):
                        plt.axvline(x = z[i], linestyle = '-.')
                plt.show()
                return ('-Inf','Inf',z)
        if a1!=0 and a2!=0:
            plt.plot(x,y)
            if len(z)>0:
                for i in range(len(z)):
                    plt.axvline(x = z[i], linestyle = '-.')
            plt.axhline(y = a1/a2, linestyle = '-.')
            plt.show()
            return (a1/a2,a1/a2,z)
        if a1==0 and a2==0:
            if b1==0 and b2!=0:
                plt.plot(x,y)
                if len(z)>0:
                    for i in range(len(z)):
                        plt.axvline(x = z[i], linestyle = '-.')
                plt.axhline(y = 0, linestyle = '-.')
                plt.show()
                return (0,0,z)
            if b1!=0 and b2==0:
                if b1*c2>0:
                    plt.plot(x,y)
                    if len(z)>0:
                        for i in range(len(z)):
                            plt.axvline(x = z[i], linestyle = '-.')
                    plt.show()
                    return ("Inf","-Inf",z)
                elif b1*c2==0:
                    plt.plot(x,y)
                    if len(z)>0:
                        for i in range(len(z)):
                            plt.axvline(x = z[i], linestyle = '-.')
                    plt.show()
                    return ("Inf","-Inf",z)    
                else:
                    plt.plot(x,y)
                    if len(z)>0:
                        for i in range(len(z)):
                            plt.axvline(x = z[i], linestyle = '-.')
                    plt.show()
                    return ("-Inf","Inf",z)
            if b1!=0 and b2!=0:
                plt.plot(x,y)
                if len(z)>0:
                    for i in range(len(z)):
                        plt.axvline(x = z[i], linestyle = '-.')
                plt.axhline(y = b1/b2, linestyle = '-.')
                plt.show()
                return (b1/b2,b1/b2,z)
            if b1==0 and b2==0:
                if c1==0 and c2!=0:
                    plt.plot(x,y)
                    if len(z)>0:
                        for i in range(len(z)):
                            plt.axvline(x = z[i], linestyle = '-.')
                    plt.axhline(y = 0, linestyle = '-.')
                    plt.show()
                    return (0,0,z)
                if c1!=0 and c2==0:
                    return 'Err'
                if c1!=0 and c2!=0:
                    plt.plot(x,y)
                    if len(z)>0:
                        for i in range(len(z)):
                            plt.axvline(x = z[i], linestyle = '-.')
                    plt.axhline(y = c1/c2, linestyle = '-.')
                    plt.show()
                    return (c1/c2,c1/c2,z)
                if c1==0 and c2==0:
                    return 'Err'
    else:
        return 'Err'

def lim(a1,b1,c1,a2,b2,c2):
    
    import matplotlib.pyplot as plt
    
    f1=plt.figure()
    
    f1.suptitle("Limit at zero")
    f1.supxlabel("X")
    f1.supylabel("Y")
    
    res1=limzero(a1,b1,c1,a2,b2,c2)
    
    f2=plt.figure()
    
    f2.suptitle("Limit at infinity")
    f2.supxlabel("X")
    f2.supylabel("Y")
    
    res2=liminf(a1,b1,c1,a2,b2,c2)
    
    return (res1, res2)