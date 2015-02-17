start: (NEWLINE|COMMENT|main)+;

main: object_stm NEWLINE? (object)+;

object_stm: '\[OBJECT:[\w_]+\]';

object:  OBJECT NEWLINE? options;

options: (COMMENT|option|NEWLINE)+;
option: TOKEN NEWLINE?;


OBJECT: '\[ITEM_[^\]]+\]'
{
    start:  '\[ITEM_' token_type ':' token_item_name RSQB;
    token_type: '[\w_]+';
    token_item_name: '[\w_]+';

    WS: '[\t \f]+' (%ignore);
    LSQB: '\[';
    RSQB: '\]';
};

TOKEN: LSQB '[\w\-: _]+' RSQB
{
    start: LSQB tokens RSQB;
    tokens:  token (':' token)*;
    token: '\w[\w\-_ ]*';

    WS: '[\t \f]+' (%ignore);
    LSQB: '\[';
    RSQB: '\]';
};

COMMENT:'[^\[\]\r?\n]+' (%ignore);
NEWLINE: '[\r?\n]+' (%newline)(%ignore) ;

LSQB: '\[';
RSQB: '\]';
