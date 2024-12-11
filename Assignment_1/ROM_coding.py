for i in range (2**7):
    inp=bin(i)[2:];n=len(inp)
    for count in range (7-n):
        inp="0"+inp
    OP=inp[0:5]
    I=inp[5]
    IsEq=inp[6]
    add=0
    if (OP=="00000"):
        add=1
    sub=0
    if (OP=="00001"):
        sub=1
    cmp=0
    if (OP=="00101"):
        cmp=1
    ld=0
    if (OP=="01110"):
        ld=1
    st=0
    if (OP=="01111"):
        st=1
    beq=0
    if (OP=="10000"):
        beq=1
    call=0
    if (OP=="10011"):
        call=1
    ret=0
    if (OP=="10100"):
        ret=1
    hlt=0
    if (OP=="11111"):
        hlt=1

    alu_sel="0000"
    if (add):
        alu_sel="0000"
    elif (sub):
        alu_sel="0001"
    
    add1=0
    if (add or ld or st or beq):
        add1=1
    
    pcsel=str(int(beq and IsEq=="1") or ret)+str(int(ret or call))
    rs2_rd_sel=str(int(st))
    WBSel=str(int(st))
    ASel=str(int(beq or call))
    Wpc=str(int(call))
    RegWEn=str(int(add or sub or ld))
    FlWEn=str(int(cmp))
    BSel=str(int(I))
    out=RegWEn+BSel+FlWEn+alu_sel+rs2_rd_sel+WBSel+ASel+pcsel+Wpc+str(hlt)
    out_str=hex(int(out,2))[2:];n=len(out_str)
    for count in range(4-n):
        out_str="0"+out_str
    print(out_str,end=" ")
    if (((i+1)%8)==0):
        print()