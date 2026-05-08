grammar compilador;

inicio:
                      'Lenguaje' '{' instrucciones* '}'
                      ;

instrucciones:
                      declaracionVariables
                      |
                      asignacionVariables
                      ;

declaracionVariables:
                      ENTERO VAR ';'           # Declaracion // entero variable1;
                      ;

asignacionVariables:
                      VAR '=' expr ';'       # Asignacion    // a = 10;
                      ;


expr
    : expr op=('*'|'/') expr   # MulDiv
    | expr op=('+'|'-') expr   # SumRes
    | '(' expr ')'             # Parentesis
    | NUM                      # Numero
    | VAR                      # Variable     // ← nuevo
    ;


/*********** LEXER  ************/

ENTERO: 'entero';
VAR : [a-zA-Z_][a-zA-Z_0-9]* ;   // nombre de variable
NUM : [0-9]+ ('.' [0-9]+)? ;
WS  : [ \t\r\n]+ -> skip ;