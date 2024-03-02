% Лабораторная работа № 1.1. Раскрутка самоприменимого компилятора
% 12 февраля 2024 г.
% Кабанов Андрей Юрьевич, ИУ9-62Б

# Цель работы
Целью данной работы является ознакомление с раскруткой 
самоприменимых компиляторов на примере модельного компилятора.

# Индивидуальный вариант
Компилятор **BeRo**. Разрешить возможность не писать ключевое слово `then` после условия в блоке `if`.


# Реализация

Различие между файлами `btpc64.pas` и `btpc64-2.pas`:

```diff
--- btpc64.pas	2020-02-15 14:28:08.000000000 +0300
+++ btpc64-2.pas	2024-02-12 17:37:45.569791393 +0300
@@ -1416,7 +1416,9 @@
   GetSymbol;
   Expression(t);
   MustBe(TypeBOOL,t);
-  Expect(SymTHEN);
+  if CurrentSymbol=SymTHEN then begin
+   GetSymbol;
+  end;
   i:=CodeLabel;
   EmitOpcode(OPJZ,0);
   Statement;

```

Различие между файлами `btpc64-2.pas` и `btpc64-3.pas`:

```diff
--- btpc64-2.pas	2024-02-12 17:37:45.569791393 +0300
+++ btpc64-3.pas	2024-02-12 17:54:10.761433419 +0300
@@ -1389,17 +1389,17 @@
     end else begin
      EmitAddressVar(i);
     end;
-    if Types[t].Kind=KindSIMPLE then begin
+    if Types[t].Kind=KindSIMPLE begin
      EmitOpcode2(OPStore);
     end else begin
      EmitOpcode(OPMove,Types[t].Size);
     end;
    end;
    IdFUNC:begin
-    if Identifiers[i].TypeDefinition=0 then begin
+    if Identifiers[i].TypeDefinition=0 begin
      FunctionCall(i);
     end else begin
-     if not Identifiers[i].Inside then begin
+     if not Identifiers[i].Inside begin
       Error(122);
      end;
      GetSymbol;
@@ -1412,17 +1412,17 @@
    end;
    IdCONST,IdFIELD,IdTYPE:Error(123);
   end;
- end else if CurrentSymbol=SymIF then begin
+ end else if CurrentSymbol=SymIF begin
   GetSymbol;
   Expression(t);
   MustBe(TypeBOOL,t);
-  if CurrentSymbol=SymTHEN then begin
+  if CurrentSymbol=SymTHEN begin
    GetSymbol;
   end;
   i:=CodeLabel;
   EmitOpcode(OPJZ,0);
   Statement;
-  if CurrentSymbol=SymELSE then begin
+  if CurrentSymbol=SymELSE begin
    GetSymbol;
    j:=CodeLabel;
    EmitOpcode(OPJmp,0);
@@ -1431,7 +1431,7 @@
    Statement;
   end;
   Code[i+1]:=CodeLabel;
- end else if CurrentSymbol=SymCASE then begin
+ end else if CurrentSymbol=SymCASE begin
   GetSymbol;
   Expression(t);
   MustBe(TypeINT,t);

```

# Тестирование

Тестовый пример:

```pascal
program Hello;

begin
  if 10 = 10 begin
    WriteLn('Hello, student!');
  end;
end.
```

Вывод тестового примера на `stdout`

```
Hello, student!
```

# Вывод
При выполнении лабораторной работы мы изучили устройство 
компилятора **BeRo** и научились при помощи раскрутки создавать 
самоприменимый компилятор.