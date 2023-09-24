# XWin-LM-usage

## Preparation

```sh
bash prepare.sh
```

## Execution

Note that different executions return different results.

```sh
[mizushima]$ bash chat.sh
以下にJavaに翻訳したコードを示します。C言語のポインタはJavaでは参照に該当することに注意しています。また、Javaでは変数へ
の参照を取得する機能（Cでの&a）はないため、xとyの型も変える必要があります。
```java
public void s(int[] a, int[] b) {
    int t = a[0];
    a[0] = b[0];
    b[0] = t;
}

public class Main {
    public static void main(String[] args) {
        int x = 100, y = 200;
        s(x, y);
        System.out.println("x = " + x + ", y = " + y);
    }
}
```
このJavaコードは、C言語のプログラムをJavaに翻訳したものです。s関数は、xとyの値を交換する役割を持っています。mainメソッドでは、xとyの値を設定し、s関数を呼び出して、xとyの値を出力します。
```
