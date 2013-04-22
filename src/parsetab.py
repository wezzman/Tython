
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = '\xfd"H\x03\x9eq\xef-\xd5\x13\xce\x9d\xb0\xae\x10\xa5'
    
_lr_action_items = {'RParen':([1,4,5,6,12,13,16,17,19,20,21,],[-7,-8,-10,-9,19,-11,-5,-4,-12,-2,-3,]),'Name':([0,3,9,10,11,14,15,22,],[2,13,13,13,2,13,13,2,]),'NewLine':([1,2,4,5,6,8,13,16,17,18,19,20,21,23,],[-7,-11,-8,-10,-9,-6,-11,-5,-4,22,-12,-2,-3,-1,]),'Equal':([2,],[11,]),'Times':([1,2,4,5,6,13,16,17,19,20,21,],[10,-11,-8,-10,-9,-11,-5,-4,-12,10,10,]),'Plus':([1,2,4,5,6,8,12,13,16,17,19,20,21,],[-7,-11,-8,-10,-9,14,14,-11,-5,-4,-12,-2,-3,]),'LParen':([0,3,9,10,11,14,15,22,],[3,3,3,3,3,3,3,3,]),'Integer':([0,3,9,10,11,14,15,22,],[6,6,6,6,6,6,6,6,]),'Floating':([0,3,9,10,11,14,15,22,],[5,5,5,5,5,5,5,5,]),'$end':([1,2,4,5,6,7,8,13,16,17,19,20,21,23,],[-7,-11,-8,-10,-9,0,-6,-11,-5,-4,-12,-2,-3,-1,]),'Minus':([1,2,4,5,6,8,12,13,16,17,19,20,21,],[-7,-11,-8,-10,-9,15,15,-11,-5,-4,-12,-2,-3,]),'Divide':([1,2,4,5,6,13,16,17,19,20,21,],[9,-11,-8,-10,-9,-11,-5,-4,-12,9,9,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'line':([0,11,22,],[7,18,23,]),'expression':([0,3,11,22,],[8,12,8,8,]),'term':([0,3,11,14,15,22,],[1,1,1,20,21,1,]),'factor':([0,3,9,10,11,14,15,22,],[4,4,16,17,4,4,4,4,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> line","S'",1,None,None,None),
  ('line -> Name Equal line NewLine line','line',5,'p_var_declaration','/home/michael/Dropbox/Workspace/Tython/src/calc_lex.py',56),
  ('expression -> expression Plus term','expression',3,'p_bin_op','/home/michael/Dropbox/Workspace/Tython/src/calc_lex.py',61),
  ('expression -> expression Minus term','expression',3,'p_bin_op','/home/michael/Dropbox/Workspace/Tython/src/calc_lex.py',62),
  ('term -> term Times factor','term',3,'p_bin_op','/home/michael/Dropbox/Workspace/Tython/src/calc_lex.py',63),
  ('term -> term Divide factor','term',3,'p_bin_op','/home/michael/Dropbox/Workspace/Tython/src/calc_lex.py',64),
  ('line -> expression','line',1,'p_term_factor','/home/michael/Dropbox/Workspace/Tython/src/calc_lex.py',76),
  ('expression -> term','expression',1,'p_term_factor','/home/michael/Dropbox/Workspace/Tython/src/calc_lex.py',77),
  ('term -> factor','term',1,'p_term_factor','/home/michael/Dropbox/Workspace/Tython/src/calc_lex.py',78),
  ('factor -> Integer','factor',1,'p_term_factor','/home/michael/Dropbox/Workspace/Tython/src/calc_lex.py',79),
  ('factor -> Floating','factor',1,'p_term_factor','/home/michael/Dropbox/Workspace/Tython/src/calc_lex.py',80),
  ('factor -> Name','factor',1,'p_term_var_name','/home/michael/Dropbox/Workspace/Tython/src/calc_lex.py',85),
  ('factor -> LParen expression RParen','factor',3,'p_paren_factor','/home/michael/Dropbox/Workspace/Tython/src/calc_lex.py',89),
]
