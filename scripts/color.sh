#!/bin/bash
# ������ɫ����, ���ǵð�, \033��\e��\E�ǵȼ۵�
RED='\E[1;31m'       # ��
GREEN='\E[1;32m'    # ��
YELOW='\E[1;33m'    # ��
BLUE='\E[1;34m'     # ��
PINK='\E[1;35m'     # �ۺ�
RES='\E[0m'          # �����ɫ
 
 
# ����ʹ��ʱ, ����ͨ��echo -e������
echo -e  "${RED}Red color${RES}"
echo -e  "${YELOW}Yelow color${RES}"
echo -e  "${BLUE}Blue color${RES}"
echo -e  "${GREEN}Green color${RES}"
echo -e  "${PINK}Pink color${RES}"
