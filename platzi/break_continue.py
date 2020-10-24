def run():
    for contador in range(20):
        if contador %2 != 0:
            continue
        print(contador)

    for i in range(100):
        print(i)
        if i ==10:
            break
    

if __name__=='__main__':
    run()
