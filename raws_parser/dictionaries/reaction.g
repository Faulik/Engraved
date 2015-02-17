start: (NEWLINE|COMMENT|main)+;

main: object_stm NEWLINE? (object)+;

object_stm: '\[OBJECT:[\w_]+\]';

object:  OBJECT NEWLINE? options;

options: (COMMENT|option|NEWLINE)+;
option: TOKEN NEWLINE?;


OBJECT: '\[REACTION:[^\]]+\]'
{
    start:  '\[REACTION:' tokens RSQB;
    tokens: token_item_name;
    token_item_name: '[\w_]+';

    WS: '[\t \f]+' (%ignore);
    LSQB: '\[';
    RSQB: '\]';
};

TOKEN: LSQB '[^\[\]]+' RSQB
{
    start: LSQB tokens RSQB;
    @tokens:  token (COLON token)*;
    token: '[^\[\]:]+';

    WS: '[\t \f]+' (%ignore);
    COLON: ':';
    LSQB: '\[';
    RSQB: '\]';
};

COMMENT:'[^\[\]\r?\n]+' (%ignore);
NEWLINE: '[\r?\n]+' (%newline)(%ignore) ;

LSQB: '\[';
RSQB: '\]';
