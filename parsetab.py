
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'programnonassocANDORnonassocEQUALNOTEQUALnonassocLESSLESSEQUALGREATERGREATEREQUALleftPLUSMINUSleftTIMESDIVIDEleftMODCONCATrightUMINUSNOTAND ASSIGN COMMA CONCAT DIVIDE DO ELSE END EQUAL FUNCTION GREATER GREATEREQUAL ID IF LESS LESSEQUAL LOCAL LPAREN MINUS MOD NOT NOTEQUAL NUMBER OR PLUS RETURN RPAREN SEMICOLON STRING THEN TIMES VAR WHILEempty :program : blockblock : blocklistblocklist : command blockterminator blocklist\n                 | emptyblockterminator : empty\n                       | SEMICOLONcommand : ID ASSIGN exp\n               | functioncall\n               | vardeclaration\n               | localdeclaration\n               | functiondeclaration\n               | varassignmultiple\n               | WHILE exp DO block END\n               | IF exp THEN block elsestnt END\n               | RETURN explistexpassign : ASSIGN exp\n                 | emptylocaldeclaration : LOCAL ID expassignvarassignmultiple : LOCAL ID COMMA ID ASSIGN functioncallvardeclaration : VAR ID expassignfunctiondeclaration : LOCAL FUNCTION ID LPAREN paramlist RPAREN block ENDfunctioncall : ID LPAREN explist RPARENparamlist : empty\n                 | paramseqparamseq : ID\n                | ID COMMA paramseqexplist : empty\n               | exp\n               | exp COMMA explistexp : NUMBER\n           | ID\n           | STRING\n           | functioncall\n           | exp PLUS exp\n           | exp MINUS exp\n           | exp TIMES exp\n           | exp DIVIDE exp\n           | exp MOD exp\n           | exp AND exp\n           | exp OR exp\n           | exp LESS exp\n           | exp LESSEQUAL exp\n           | exp GREATER exp\n           | exp GREATEREQUAL exp\n           | exp EQUAL exp\n           | exp NOTEQUAL exp\n           | exp CONCAT exp\n           | NOT exp\n           | MINUS exp %prec UMINUSelsestnt : empty\n                | ELSE block'
    
_lr_action_items = {'ID':([0,4,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,23,24,25,26,27,28,30,31,32,33,34,35,37,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,81,82,84,85,88,89,94,97,98,99,102,],[6,-1,-9,-10,-11,-12,-13,24,24,24,33,34,6,-6,-7,24,24,-31,-32,-33,-34,24,24,-16,-28,-29,-1,-1,63,-8,6,24,24,24,24,24,24,24,24,24,24,24,24,24,24,-50,-49,6,24,-21,24,-18,-19,83,-23,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-30,-17,90,-14,6,96,-15,-20,90,6,-22,]),'WHILE':([0,4,7,8,9,10,11,14,17,18,19,23,24,25,26,30,31,32,33,34,37,39,54,55,56,57,58,60,61,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,81,82,85,88,94,97,99,102,],[12,-1,-9,-10,-11,-12,-13,-1,12,-6,-7,-31,-32,-33,-34,-16,-28,-29,-1,-1,-8,12,-50,-49,12,-1,-21,-18,-19,-23,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-30,-17,-14,12,-15,-20,12,-22,]),'IF':([0,4,7,8,9,10,11,14,17,18,19,23,24,25,26,30,31,32,33,34,37,39,54,55,56,57,58,60,61,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,81,82,85,88,94,97,99,102,],[13,-1,-9,-10,-11,-12,-13,-1,13,-6,-7,-31,-32,-33,-34,-16,-28,-29,-1,-1,-8,13,-50,-49,13,-1,-21,-18,-19,-23,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-30,-17,-14,13,-15,-20,13,-22,]),'RETURN':([0,4,7,8,9,10,11,14,17,18,19,23,24,25,26,30,31,32,33,34,37,39,54,55,56,57,58,60,61,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,81,82,85,88,94,97,99,102,],[14,-1,-9,-10,-11,-12,-13,-1,14,-6,-7,-31,-32,-33,-34,-16,-28,-29,-1,-1,-8,14,-50,-49,14,-1,-21,-18,-19,-23,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-30,-17,-14,14,-15,-20,14,-22,]),'$end':([0,1,2,3,4,5,7,8,9,10,11,14,17,18,19,23,24,25,26,30,31,32,33,34,36,37,54,55,57,58,60,61,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,81,82,85,94,97,102,],[-1,0,-2,-3,-1,-5,-9,-10,-11,-12,-13,-1,-1,-6,-7,-31,-32,-33,-34,-16,-28,-29,-1,-1,-4,-8,-50,-49,-1,-21,-18,-19,-23,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-30,-17,-14,-15,-20,-22,]),'VAR':([0,4,7,8,9,10,11,14,17,18,19,23,24,25,26,30,31,32,33,34,37,39,54,55,56,57,58,60,61,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,81,82,85,88,94,97,99,102,],[15,-1,-9,-10,-11,-12,-13,-1,15,-6,-7,-31,-32,-33,-34,-16,-28,-29,-1,-1,-8,15,-50,-49,15,-1,-21,-18,-19,-23,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-30,-17,-14,15,-15,-20,15,-22,]),'LOCAL':([0,4,7,8,9,10,11,14,17,18,19,23,24,25,26,30,31,32,33,34,37,39,54,55,56,57,58,60,61,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,81,82,85,88,94,97,99,102,],[16,-1,-9,-10,-11,-12,-13,-1,16,-6,-7,-31,-32,-33,-34,-16,-28,-29,-1,-1,-8,16,-50,-49,16,-1,-21,-18,-19,-23,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-30,-17,-14,16,-15,-20,16,-22,]),'END':([3,4,5,7,8,9,10,11,14,17,18,19,23,24,25,26,30,31,32,33,34,36,37,39,54,55,56,57,58,60,61,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,85,86,87,88,94,95,97,99,101,102,],[-3,-1,-5,-9,-10,-11,-12,-13,-1,-1,-6,-7,-31,-32,-33,-34,-16,-28,-29,-1,-1,-4,-8,-1,-50,-49,-1,-1,-21,-18,-19,-23,85,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-1,-30,-17,-14,94,-51,-1,-15,-52,-20,-1,102,-22,]),'ELSE':([3,4,5,7,8,9,10,11,14,17,18,19,23,24,25,26,30,31,32,33,34,36,37,54,55,56,57,58,60,61,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,85,94,97,102,],[-3,-1,-5,-9,-10,-11,-12,-13,-1,-1,-6,-7,-31,-32,-33,-34,-16,-28,-29,-1,-1,-4,-8,-50,-49,-1,-1,-21,-18,-19,-23,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,88,-30,-17,-14,-15,-20,-22,]),'SEMICOLON':([4,7,8,9,10,11,14,23,24,25,26,30,31,32,33,34,37,54,55,57,58,60,61,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,81,82,85,94,97,102,],[19,-9,-10,-11,-12,-13,-1,-31,-32,-33,-34,-16,-28,-29,-1,-1,-8,-50,-49,-1,-21,-18,-19,-23,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-30,-17,-14,-15,-20,-22,]),'ASSIGN':([6,33,34,83,],[20,59,59,89,]),'LPAREN':([6,24,63,96,],[21,21,84,21,]),'NUMBER':([12,13,14,20,21,27,28,40,41,42,43,44,45,46,47,48,49,50,51,52,53,57,59,],[23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,]),'STRING':([12,13,14,20,21,27,28,40,41,42,43,44,45,46,47,48,49,50,51,52,53,57,59,],[25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,]),'NOT':([12,13,14,20,21,27,28,40,41,42,43,44,45,46,47,48,49,50,51,52,53,57,59,],[28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'MINUS':([12,13,14,20,21,22,23,24,25,26,27,28,29,32,37,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,57,59,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,82,],[27,27,27,27,27,41,-31,-32,-33,-34,27,27,41,41,41,27,27,27,27,27,27,27,27,27,27,27,27,27,27,-50,-49,27,27,-23,-35,-36,-37,-38,-39,41,41,41,41,41,41,41,41,-48,41,]),'FUNCTION':([16,],[35,]),'RPAREN':([21,23,24,25,26,31,32,38,54,55,57,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,81,84,90,91,92,93,100,],[-1,-31,-32,-33,-34,-28,-29,64,-50,-49,-1,-23,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-30,-1,-26,99,-24,-25,-27,]),'DO':([22,23,24,25,26,54,55,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,],[39,-31,-32,-33,-34,-50,-49,-23,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,]),'PLUS':([22,23,24,25,26,29,32,37,54,55,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,82,],[40,-31,-32,-33,-34,40,40,40,-50,-49,-23,-35,-36,-37,-38,-39,40,40,40,40,40,40,40,40,-48,40,]),'TIMES':([22,23,24,25,26,29,32,37,54,55,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,82,],[42,-31,-32,-33,-34,42,42,42,-50,-49,-23,42,42,-37,-38,-39,42,42,42,42,42,42,42,42,-48,42,]),'DIVIDE':([22,23,24,25,26,29,32,37,54,55,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,82,],[43,-31,-32,-33,-34,43,43,43,-50,-49,-23,43,43,-37,-38,-39,43,43,43,43,43,43,43,43,-48,43,]),'MOD':([22,23,24,25,26,29,32,37,54,55,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,82,],[44,-31,-32,-33,-34,44,44,44,-50,-49,-23,44,44,44,44,-39,44,44,44,44,44,44,44,44,-48,44,]),'AND':([22,23,24,25,26,29,32,37,54,55,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,82,],[45,-31,-32,-33,-34,45,45,45,-50,-49,-23,-35,-36,-37,-38,-39,None,None,-42,-43,-44,-45,-46,-47,-48,45,]),'OR':([22,23,24,25,26,29,32,37,54,55,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,82,],[46,-31,-32,-33,-34,46,46,46,-50,-49,-23,-35,-36,-37,-38,-39,None,None,-42,-43,-44,-45,-46,-47,-48,46,]),'LESS':([22,23,24,25,26,29,32,37,54,55,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,82,],[47,-31,-32,-33,-34,47,47,47,-50,-49,-23,-35,-36,-37,-38,-39,47,47,None,None,None,None,47,47,-48,47,]),'LESSEQUAL':([22,23,24,25,26,29,32,37,54,55,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,82,],[48,-31,-32,-33,-34,48,48,48,-50,-49,-23,-35,-36,-37,-38,-39,48,48,None,None,None,None,48,48,-48,48,]),'GREATER':([22,23,24,25,26,29,32,37,54,55,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,82,],[49,-31,-32,-33,-34,49,49,49,-50,-49,-23,-35,-36,-37,-38,-39,49,49,None,None,None,None,49,49,-48,49,]),'GREATEREQUAL':([22,23,24,25,26,29,32,37,54,55,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,82,],[50,-31,-32,-33,-34,50,50,50,-50,-49,-23,-35,-36,-37,-38,-39,50,50,None,None,None,None,50,50,-48,50,]),'EQUAL':([22,23,24,25,26,29,32,37,54,55,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,82,],[51,-31,-32,-33,-34,51,51,51,-50,-49,-23,-35,-36,-37,-38,-39,51,51,-42,-43,-44,-45,None,None,-48,51,]),'NOTEQUAL':([22,23,24,25,26,29,32,37,54,55,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,82,],[52,-31,-32,-33,-34,52,52,52,-50,-49,-23,-35,-36,-37,-38,-39,52,52,-42,-43,-44,-45,None,None,-48,52,]),'CONCAT':([22,23,24,25,26,29,32,37,54,55,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,82,],[53,-31,-32,-33,-34,53,53,53,-50,-49,-23,53,53,53,53,-39,53,53,53,53,53,53,53,53,-48,53,]),'THEN':([23,24,25,26,29,54,55,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,],[-31,-32,-33,-34,56,-50,-49,-23,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,]),'COMMA':([23,24,25,26,32,34,54,55,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,90,],[-31,-32,-33,-34,57,62,-50,-49,-23,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,98,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'block':([0,39,56,88,99,],[2,65,80,95,101,]),'blocklist':([0,17,39,56,88,99,],[3,36,3,3,3,3,]),'command':([0,17,39,56,88,99,],[4,4,4,4,4,4,]),'empty':([0,4,14,17,21,33,34,39,56,57,80,84,88,99,],[5,18,31,5,31,60,60,5,5,31,87,92,5,5,]),'functioncall':([0,12,13,14,17,20,21,27,28,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,56,57,59,88,89,99,],[7,26,26,26,7,26,26,26,26,7,26,26,26,26,26,26,26,26,26,26,26,26,26,26,7,26,26,7,97,7,]),'vardeclaration':([0,17,39,56,88,99,],[8,8,8,8,8,8,]),'localdeclaration':([0,17,39,56,88,99,],[9,9,9,9,9,9,]),'functiondeclaration':([0,17,39,56,88,99,],[10,10,10,10,10,10,]),'varassignmultiple':([0,17,39,56,88,99,],[11,11,11,11,11,11,]),'blockterminator':([4,],[17,]),'exp':([12,13,14,20,21,27,28,40,41,42,43,44,45,46,47,48,49,50,51,52,53,57,59,],[22,29,32,37,32,54,55,66,67,68,69,70,71,72,73,74,75,76,77,78,79,32,82,]),'explist':([14,21,57,],[30,38,81,]),'expassign':([33,34,],[58,61,]),'elsestnt':([80,],[86,]),'paramlist':([84,],[91,]),'paramseq':([84,98,],[93,100,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',26),
  ('program -> block','program',1,'p_program','parser.py',30),
  ('block -> blocklist','block',1,'p_block','parser.py',34),
  ('blocklist -> command blockterminator blocklist','blocklist',3,'p_blocklist','parser.py',38),
  ('blocklist -> empty','blocklist',1,'p_blocklist','parser.py',39),
  ('blockterminator -> empty','blockterminator',1,'p_blockterminator','parser.py',46),
  ('blockterminator -> SEMICOLON','blockterminator',1,'p_blockterminator','parser.py',47),
  ('command -> ID ASSIGN exp','command',3,'p_command','parser.py',51),
  ('command -> functioncall','command',1,'p_command','parser.py',52),
  ('command -> vardeclaration','command',1,'p_command','parser.py',53),
  ('command -> localdeclaration','command',1,'p_command','parser.py',54),
  ('command -> functiondeclaration','command',1,'p_command','parser.py',55),
  ('command -> varassignmultiple','command',1,'p_command','parser.py',56),
  ('command -> WHILE exp DO block END','command',5,'p_command','parser.py',57),
  ('command -> IF exp THEN block elsestnt END','command',6,'p_command','parser.py',58),
  ('command -> RETURN explist','command',2,'p_command','parser.py',59),
  ('expassign -> ASSIGN exp','expassign',2,'p_expassign','parser.py',74),
  ('expassign -> empty','expassign',1,'p_expassign','parser.py',75),
  ('localdeclaration -> LOCAL ID expassign','localdeclaration',3,'p_localdeclaration','parser.py',83),
  ('varassignmultiple -> LOCAL ID COMMA ID ASSIGN functioncall','varassignmultiple',6,'p_varassignmultiple','parser.py',93),
  ('vardeclaration -> VAR ID expassign','vardeclaration',3,'p_vardeclaration','parser.py',102),
  ('functiondeclaration -> LOCAL FUNCTION ID LPAREN paramlist RPAREN block END','functiondeclaration',8,'p_functiondeclaration','parser.py',111),
  ('functioncall -> ID LPAREN explist RPAREN','functioncall',4,'p_functioncall','parser.py',122),
  ('paramlist -> empty','paramlist',1,'p_paramlist','parser.py',138),
  ('paramlist -> paramseq','paramlist',1,'p_paramlist','parser.py',139),
  ('paramseq -> ID','paramseq',1,'p_paramseq','parser.py',143),
  ('paramseq -> ID COMMA paramseq','paramseq',3,'p_paramseq','parser.py',144),
  ('explist -> empty','explist',1,'p_explist','parser.py',151),
  ('explist -> exp','explist',1,'p_explist','parser.py',152),
  ('explist -> exp COMMA explist','explist',3,'p_explist','parser.py',153),
  ('exp -> NUMBER','exp',1,'p_exp','parser.py',160),
  ('exp -> ID','exp',1,'p_exp','parser.py',161),
  ('exp -> STRING','exp',1,'p_exp','parser.py',162),
  ('exp -> functioncall','exp',1,'p_exp','parser.py',163),
  ('exp -> exp PLUS exp','exp',3,'p_exp','parser.py',164),
  ('exp -> exp MINUS exp','exp',3,'p_exp','parser.py',165),
  ('exp -> exp TIMES exp','exp',3,'p_exp','parser.py',166),
  ('exp -> exp DIVIDE exp','exp',3,'p_exp','parser.py',167),
  ('exp -> exp MOD exp','exp',3,'p_exp','parser.py',168),
  ('exp -> exp AND exp','exp',3,'p_exp','parser.py',169),
  ('exp -> exp OR exp','exp',3,'p_exp','parser.py',170),
  ('exp -> exp LESS exp','exp',3,'p_exp','parser.py',171),
  ('exp -> exp LESSEQUAL exp','exp',3,'p_exp','parser.py',172),
  ('exp -> exp GREATER exp','exp',3,'p_exp','parser.py',173),
  ('exp -> exp GREATEREQUAL exp','exp',3,'p_exp','parser.py',174),
  ('exp -> exp EQUAL exp','exp',3,'p_exp','parser.py',175),
  ('exp -> exp NOTEQUAL exp','exp',3,'p_exp','parser.py',176),
  ('exp -> exp CONCAT exp','exp',3,'p_exp','parser.py',177),
  ('exp -> NOT exp','exp',2,'p_exp','parser.py',178),
  ('exp -> MINUS exp','exp',2,'p_exp','parser.py',179),
  ('elsestnt -> empty','elsestnt',1,'p_elsestnt','parser.py',197),
  ('elsestnt -> ELSE block','elsestnt',2,'p_elsestnt','parser.py',198),
]
