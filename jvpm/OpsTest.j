.bytecode 52.0              ;Java 8
.source OpsTest.j           ;name of Jasmin file
.class public OpsTest		;Class name
.super java/lang/Object		;Belongs to Object



.method public static main([Ljava/lang/String;)V
    .limit stack 3          ;Max stack depth
    .limit locals 1         ;Locals + args = 0 + 1 = 1

<<<<<<< HEAD
    iconst_0        ; Stack: 0
    iconst_1        ; Stack: 0, 1
    iadd            ; Stack: (0+1=1)
    istore_0        ; Stack: <none>         Locals: [1][][][]
    iload_0         ; Stack: 1              Locals: [1][][][]
    iconst_3        ; Stack: 1, 3
    isub            ; Stack: (1-3=-2)
    istore_1        ; Stack: <none>         Locals: [1][-2][][]
    iload_1         ; Stack: -2             Locals: [1][-2][][]
    iconst_m1       ; Stack: -2, -1
    imul            ; Stack: (-2*-1=2)
    istore_2        ; Stack: <none>         Locals: [1][-2][2][]
    iload_2         ; Stack: 1              Locals: [1][-2][2][]
    iconst_2        ; Stack: 2, 2
    idiv            ; Stack: (2/2=1)
    istore_3        ; Stack: <none>         Locals: [1][-2][2][1]
    iload_3         ; Stack: 1              Locals: [1][-2][2][1]
    iconst_4        ; Stack: 1, 4
    iadd            ; Stack: (1+4=5)
    istore_0        ; Stack: <none>         Locals: [5][-2][2][1]
    iload_0         ; Stack: 5              Locals: [5][-2][2][1]
    iconst_2        ; Stack: 5, 2
    irem            ; Stack: (5/2=2r1)
    istore_1        ; Stack: <none>         Locals: [5][1][2][1]
    iload_1         ; Stack: 1              Locals: [5][1][2][1]
    ineg            ; Stack: (!1=-2)
    istore_2        ; Stack: <none>         Locals: [5][1][-2][1]
    iload_2         ; Stack: -2             Locals: [5][1][-2][1]
    iconst_5        ; Stack: -2, 5
    iand            ; Stack: (-2&5=4)
    istore_3        ; Stack: <none>         Locals: [5][1][-2][4]
    iload_3         ; Stack: 4              Locals: [5][1][-2][4]
    iconst_4        ; Stack: 4, 4
    imul            ; Stack: (4*4=16)
    istore_0        ; Stack: <none>         Locals: [16][1][-2][4]
    iload_0         ; Stack: 16             Locals: [16][1][-2][4]
    iconst_3        ; Stack: 16, 3
    ior	            ; Stack: (16|3=19)
    istore_1        ; Stack: <none>         Locals: [16][19][-2][4]
    iload_1         ; Stack: 19             Locals: [16][19][-2][4]
    iconst_5        ; Stack: 19, 5
    iconst_2        ; Stack: 19, 5, 2
    imul            ; Stack: 19, (5*2=10)
    istore_2        ; Stack: <none>         Locals: [16][19][10][4]
    iload_2         ; Stack: 10             Locals: [16][19][10][4]
    ixor            ; Stack: (19^10=25)
    istore_3        ; Stack: <none>         Locals: [16][19][10][25]
    iload_3         ; Stack: 25             Locals: [16][19][10][25]
    iconst_3        ; Stack: 25, 3
    ishl            ; Stack: (25<<3=200)
    istore_0        ; Stack: <none>         Locals: [200][19][10][25]
    iload_0         ; Stack: 200            Locals: [200][19][10][25]
    iconst_1        ; Stack: 200, 1
    ishr            ; Stack: (200>>1=100)
    istore_1        ; Stack: <none>         Locals: [200][100][10][25]
    iload_1         ; Stack: 100            Locals: [200][100][10][25]
    ineg            ; Stack: (!100=-101)
    istore_2        ; Stack: <none>         Locals: [200][100][-101][25]
    iload_2         ; Stack: -101           Locals: [200][100][-101][25]
    iconst_2        ; Stack: -101, 2
    iushr           ; Stack: (-101>LOGICAL>2=-26)
    istore_3        ; Stack: <none>         Locals: [200][100][-101][-26]
=======
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
    
>>>>>>> 0049e37e19f2f75d50889cbf9ea1765759b211ff

    return
.end method 