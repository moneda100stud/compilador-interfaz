grammar compilador;

inicio:
                      'Lenguaje' '{' instrucciones* '}'
                      ;

instrucciones:
                      declaracionVariables
                      |
                      asignacionVariables
                      |
                      condicional
                      |
                      ciclo
                      ;

declaracionVariables:
                      ENTERO VAR ';'           # Declaracion // entero variable1;
                      ;

asignacionVariables:
                      VAR '=' expr ';'       # Asignacion    // a = 10;
                      ;

condicional:
                      SI PAREN_A expr PAREN_C LLAVE_A instrucciones* LLAVE_C (SINO LLAVE_A instrucciones* LLAVE_C)? ';' # CondicionalStmt
                      ;

ciclo:
                      MIENTRAS PAREN_A expr PAREN_C LLAVE_A instrucciones* LLAVE_C # CicloStmt
                      ;

expr
    : expr op=('*'|'/') expr   # MulDiv
    | expr op=('+'|'-') expr   # SumRes
    | expr op=(GT|LT|EQ|NEQ) expr      # Comparacion
    | PAREN_A expr PAREN_C     # Parentesis
    | NUM                      # Numero
    | VAR                      # Variable     // ← nuevo
    ;


/*********** LEXER  ************/

SI: 'si';
SINO: 'sino';
MIENTRAS: 'mientras';
ENTERO: 'entero';

GT: '>';
LT: '<';
EQ: '==';
NEQ: '!=';

PAREN_A: '(';
PAREN_C: ')';
LLAVE_A: '{';
LLAVE_C: '}';

VAR : [a-zA-Z_][a-zA-Z_0-9]* ;   // nombre de variable
NUM : [0-9]+ ('.' [0-9]+)? ;
WS  : [ \t\r\n]+ -> skip ;