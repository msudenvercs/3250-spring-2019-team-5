.bytecode 52.0              ;Java 8
.source OpsTest.j           ;name of Jasmin file
.class public OpsTest		;Class name
.super java/lang/Object		;Belongs to Object



.method public static main([Ljava/lang/String;)V
    .limit stack 3          ;Max stack depth
    .limit locals 1         ;Locals + args = 0 + 1 = 1

    iconst_0        ;Stack: 0
    iconst_1        ;Stack: 0, 1
    iadd            ;Stack: (0+1=1)
    iconst_3        ;Stack: 1, 3
    isub            ;Stack: (1-3=-2)
    iconst_m1       ;Stack: -2, -1
    imul            ;Stack: (-2*-1=2)
    iconst_2        ;Stack: 2, 2
    idiv            ;Stack: (2/2=1)
    iconst_4        ;Stack: 1, 4
    iadd            ;Stack: (1+4=5)
    iconst_2        ;Stack: 5, 2
    irem            ;Stack: (5/2=2r1)
    ineg            ;Stack: (!1=-2)
    iconst_5        ;Stack: -2, 5
    iand            ;Stack: (-2&5=4)
    iconst_4        ;Stack: 4, 4
    imul            ;Stack: (4*4=16)
    iconst_3        ;Stack: 16, 3
    ior	            ;Stack: (16|3=19)
    iconst_5        ;Stack: 19, 5
    iconst_2        ;Stack: 19, 5, 2
    imul            ;Stack: 19, (5*2=10)
    ixor            ;Stack: (19^10=25)
    

    return
.end method 