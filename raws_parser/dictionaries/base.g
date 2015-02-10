start: (NEWLINE|COMMENT|objects)+;

objects: object_stm NEWLINE? (object)+;

object_stm: '\[OBJECT:[\w_]+' RSQB;

object:  OBJECT NEWLINE? tokens;

tokens: (COMMENT|token|NEWLINE)+;
token: TOKEN NEWLINE?;

OBJECT: LSQB 'ITEM_[^\]]+' RSQB
{
    start: '\[ITEM_' token_type ':' token_item_name RSQB;
    token_type: '[\w_]+';
    token_item_name: '[\w_]+';

    WS: '[\t \f]+' (%ignore);
    LSQB: '\[';
    RSQB: '\]';
};

TOKEN: LSQB '[\w: _]+' RSQB
{
    start: LSQB tokens RSQB;
    tokens:  token (':' token)*;
    token: '\w[\w_ ]*';

    WS: '[\t \f]+' (%ignore);
    LSQB: '\[';
    RSQB: '\]';
};

COMMENT:'[^\[\]\r?\n]+';
NEWLINE: '[\r?\n]+' (%newline) ;

LSQB: '\[';
RSQB: '\]';

