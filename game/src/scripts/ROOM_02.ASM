.SRC ROOM 2

.INCLUDE DEFINE.ASM

.COMMAND IDV_OPEN IDN_DOOR

DAT[$02] > $01
     PRINT IDM_IT_IS_OPEN

.COMMAND IDV_OPEN IDN_DOOR

DAT[$0c] = $01
