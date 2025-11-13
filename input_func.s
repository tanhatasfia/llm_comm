<func0>:
endbr64
push   %rbp
mov    %rsp,%rbp
mov    %rdi,-0x18(%rbp)
mov    %esi,-0x1c(%rbp)
movss  %xmm0,-0x20(%rbp)
movl   $0x0,-0x8(%rbp)
jmp    11f1 <func0+0x88>
mov    -0x8(%rbp),%eax
add    $0x1,%eax
mov    %eax,-0x4(%rbp)
jmp    11e5 <func0+0x7c>
mov    -0x8(%rbp),%eax
cltq
lea    0x0(,%rax,4),%rdx
00
mov    -0x18(%rbp),%rax
add    %rdx,%rax
movss  (%rax),%xmm0
mov    -0x4(%rbp),%eax
cltq
lea    0x0(,%rax,4),%rdx
00
mov    -0x18(%rbp),%rax
add    %rdx,%rax
movss  (%rax),%xmm1
subss  %xmm1,%xmm0
movss  0xf03(%rip),%xmm1
00
andps  %xmm0,%xmm1
movss  -0x20(%rbp),%xmm0
comiss %xmm1,%xmm0
jbe    11e1 <func0+0x78>
mov    $0x1,%eax
jmp    11fe <func0+0x95>
addl   $0x1,-0x4(%rbp)
mov    -0x4(%rbp),%eax
cmp    -0x1c(%rbp),%eax
jl     1191 <func0+0x28>
addl   $0x1,-0x8(%rbp)
mov    -0x8(%rbp),%eax
cmp    -0x1c(%rbp),%eax
jl     1186 <func0+0x1d>
mov    $0x0,%eax
pop    %rbp
ret

