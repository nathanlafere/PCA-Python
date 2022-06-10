import pygame
from pygame import K_DOWN, K_ESCAPE, K_RETURN, K_SPACE, K_UP, MOUSEBUTTONDOWN, K_z
import sys
import font_data
import glob
import pickle
import text_data



def radiobutton(x,y,selected):
    pygame.draw.circle(janela,palette[selected][1], (x,y), 5, 1)
    pygame.draw.circle(janela,palette[selected][1], (x,y), 6, 1)
    pygame.draw.circle(janela,palette[selected][1], (x,y), 7, 1)

def rbp_function(x,y,mouse_b,mouse_p,val):#RadionButtonPallete_Function
    global p_checked
    if mouse_b[0] and  x+5 >= mouse_p[0] >= x-5 and y+5 >= mouse_p[1] >= y-5:
            p_checked = val
    if p_checked == val:
        pygame.draw.circle(janela, palette[p_checked][3], (40,65+(val*20)), 5)

def rbs_function(x,y,mouse_b,mouse_p,val):#RadionButtonSize_Function
    global s_checked
    if mouse_b[0] and  x+5 >= mouse_p[0] >= x-5 and y+5 >= mouse_p[1] >= y-5:
            s_checked = val
    if s_checked == val:
        pygame.draw.circle(janela, palette[p_checked][3], (480,65+(val*20)), 5)

def button(x,y,size,mouse_b,mouse_p,function,text, b_select, b_val):
    pygame.draw.rect(janela, palette[p_checked][1], [x-4,y-4,size[0]+8,size[1]+8])
    pygame.draw.rect(janela, palette[p_checked][6], [x-2,y-2,size[0]+4,size[1]+4])
    
    if b_select == b_val or x + size[0] >= mouse_p[0] >= x and y + size[1] >= mouse_p[1] >= y:
        pygame.draw.rect(janela, palette[p_checked][4], [x,y,size[0],size[1]],False, 8)
    else:
        pygame.draw.rect(janela, palette[p_checked][1], [x,y,size[0],size[1]],False, 4)
    
    button_text = font_data.menu_font.render(text, True, palette[p_checked][3])
    janela.blit(button_text, (x + size[0]/2 - button_text.get_size()[0]/2, y + size[1]/2 - button_text.get_size()[1]/2))
    if mouse_b[0] == True and  x + size[0] >= mouse_p[0] >= x and y + size[1] >= mouse_p[1] >= y:
        if type(function) is list:
            function[0](function[1])
            function[2]()
        else:
            function()

def menu_text(x,y,text):
    locale_t = font_data.menu_font.render(text, True, palette[p_checked][3])
    janela.blit(locale_t, (x,y))

def save_data(c):
    global chose
    save_list[c] = [text_alt,chose]
    with open('saves.pkl','wb') as n:
        pickle.dump(save_list,n)
        n.close()

def del_save(c):
    save_list[c] = []
    with open('saves.pkl', 'wb') as n:
        pickle.dump(save_list,n)
        n.close()

def save_screen():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        mouse_pos = pygame.mouse.get_pos()
        mouse_b = pygame.mouse.get_pressed()
        pygame.draw.rect(janela, palette[p_checked][1], [100,100,janela.get_size()[0]-200,janela.get_size()[1]-200])
        pygame.draw.rect(janela, palette[p_checked][6], [103,103,janela.get_size()[0]-206,janela.get_size()[1]-206],2)
        save_box01 = pygame.draw.rect(janela, palette[p_checked][6], [110,110,janela.get_size()[0]-220,janela.get_size()[1]*17/100],2)
        save_box02 = pygame.draw.rect(janela, palette[p_checked][6], [110,115+janela.get_size()[1]*17/100,janela.get_size()[0]-220,janela.get_size()[1]*17/100],2)
        save_box03 = pygame.draw.rect(janela, palette[p_checked][6], [110,120+janela.get_size()[1]*17/100*2,janela.get_size()[0]-220,janela.get_size()[1]*17/100],2)
        button(janela.get_size()[0]/2-33,140+janela.get_size()[1]*17/100*3,[66,30],mouse_b,mouse_pos,backlog_menu,"Voltar",0,4)
        list_box = [save_box01,save_box02,save_box03]
        for c in range(3):
            if save_list[c]:
                save_text = font_data.save_font.render(str(save_list[c][0]*100/len(text_data.text_base))[:5]+'%', True, palette[p_checked][3])
                x = font_data.save_font.render('x', True,[200,0,0])
                janela.blit(x,[janela.get_size()[0]-130,list_box[c][1]-8])
            else:
                save_text = font_data.save_font.render('No Data', True, palette[p_checked][3])
            janela.blit(save_text,[janela.get_size()[0]/2-save_text.get_size()[0]/2,list_box[c][1]+list_box[c][3]/2-save_text.get_size()[1]/2])
            if save_list[c] and mouse_pos[0] in range(janela.get_size()[0]-130,janela.get_size()[0]-130+x.get_size()[0]) and mouse_pos[1] in range(list_box[c][1],list_box[c][1]+x.get_size()[1]-14) and mouse_b[0]:
                confirm_prompt('Deseja realmente deletar este save?',del_save,backlog_menu,c)
            elif mouse_pos[0] in range(list_box[c][0],list_box[c][0]+list_box[c][2]) and mouse_pos[1] in range(list_box[c][1],list_box[c][1]+list_box[c][3]) and mouse_b[0]:
                if save_list[c]:
                    confirm_prompt('Deseja realmente salvar sobre este save?',save_data,backlog_menu,c)
                else:
                    save_data(c)
                    backlog_menu()
        pygame.display.update()

def load_screen():
    global text_alt
    global chose
    global save_list
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        mouse_pos = pygame.mouse.get_pos()
        mouse_b = pygame.mouse.get_pressed()
        pygame.draw.rect(janela, palette[p_checked][1], [100,100,janela.get_size()[0]-200,janela.get_size()[1]-200])
        pygame.draw.rect(janela, palette[p_checked][6], [103,103,janela.get_size()[0]-206,janela.get_size()[1]-206],2)
        save_box01 = pygame.draw.rect(janela, palette[p_checked][6], [110,110,janela.get_size()[0]-220,janela.get_size()[1]*17/100],2)
        save_box02 = pygame.draw.rect(janela, palette[p_checked][6], [110,115+janela.get_size()[1]*17/100,janela.get_size()[0]-220,janela.get_size()[1]*17/100],2)
        save_box03 = pygame.draw.rect(janela, palette[p_checked][6], [110,120+janela.get_size()[1]*17/100*2,janela.get_size()[0]-220,janela.get_size()[1]*17/100],2)
        button(janela.get_size()[0]/2-33,140+janela.get_size()[1]*17/100*3,[66,30],mouse_b,mouse_pos,main_menu,"Voltar",0,4)
        list_box = [save_box01,save_box02,save_box03]
        for c in range(3):
            if save_list[c]:
                save_text = font_data.save_font.render(str(save_list[c][0]*100/len(text_data.text_base))[:5]+'%', True, palette[p_checked][3])
                x = font_data.save_font.render('x', True,[200,0,0])
                janela.blit(x,[janela.get_size()[0]-130,list_box[c][1]-8])
            else:
                save_text = font_data.save_font.render('No Data', True, palette[p_checked][3])
            janela.blit(save_text,[janela.get_size()[0]/2-save_text.get_size()[0]/2,list_box[c][1]+list_box[c][3]/2-save_text.get_size()[1]/2])
            if save_list[c] and mouse_pos[0] in range(janela.get_size()[0]-130,janela.get_size()[0]-130+x.get_size()[0]) and mouse_pos[1] in range(list_box[c][1],list_box[c][1]+x.get_size()[1]-14) and mouse_b[0]:
                confirm_prompt('Deseja realmente deletar este save?',del_save,main_menu,c)
            if mouse_pos[0] in range(list_box[c][0],list_box[c][0]+list_box[c][2]) and mouse_pos[1] in range(list_box[c][1],list_box[c][1]+list_box[c][3]) and mouse_b[0]:
                if save_list[c]:
                    with open('saves.pkl','rb') as n:
                        save_list = pickle.load(n)
                        n.close()
                    text_alt = save_list[c][0]
                    chose = save_list[c][1]
                    diag_test()

def confirm_prompt(text,function,re,c):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        mouse_pos = pygame.mouse.get_pos()
        mouse_b = pygame.mouse.get_pressed()
        pygame.draw.rect(janela, palette[p_checked][1], [janela.get_size()[0]/2-180,janela.get_size()[1]/2-80,360,160])
        pygame.draw.rect(janela, palette[p_checked][6], [janela.get_size()[0]/2-182,janela.get_size()[1]/2-82,358,158],2)
        text_conf = font_data.menu_font.render(text, True,palette[p_checked][3])
        janela.blit(text_conf,[janela.get_size()[0]/2-text_conf.get_size()[0]/2,janela.get_size()[1]/2-30-text_conf.get_size()[1]/2])
        button(janela.get_size()[0]/2-76,janela.get_size()[1]/2+30,[66,30],mouse_b,mouse_pos,[function,c,re],"Sim",0,4)
        button(janela.get_size()[0]/2+7,janela.get_size()[1]/2+30,[66,30],mouse_b,mouse_pos,re,"Não",0,4)

def backlog_menu():
    menu = True
    b_select = 0
    while menu == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    return
                if event.key == K_RETURN:
                    if b_select == 1:
                        diag_test()
                    if b_select == 2:
                        save_data()
                if event.key == K_DOWN:
                    if b_select <= 1:
                        b_select = 2
                    else:
                        b_select -= 1
                if event.key == K_UP:
                    if b_select == 2:
                        b_select = 1
                    else:
                        b_select += 1
        janela.fill(palette[p_checked][0])
        mouse_pos = pygame.mouse.get_pos()
        mouse_button = pygame.mouse.get_pressed()
        pygame.draw.rect(janela, palette[p_checked][2], direct_sizes[s_checked][3])
        pygame.draw.circle(janela, palette[p_checked][2], direct_sizes[s_checked][4][0], direct_sizes[s_checked][5][0])
        pygame.draw.circle(janela, palette[p_checked][0], direct_sizes[s_checked][4][1], direct_sizes[s_checked][5][1])
        button(direct_sizes[s_checked][2][0],direct_sizes[s_checked][2][1],direct_sizes[s_checked][2][2],mouse_button,mouse_pos,diag_test,"Voltar",b_select,1)
        button(direct_sizes[s_checked][2][0],direct_sizes[s_checked][2][1]-50,direct_sizes[s_checked][2][2],mouse_button,mouse_pos,save_screen,"Salvar",b_select,2)
        button(direct_sizes[s_checked][2][0],direct_sizes[s_checked][2][1]-100,direct_sizes[s_checked][2][2],mouse_button,mouse_pos,main_menu,"Menu",b_select,2)
        pygame.display.update()

def diag_button(alt,mouse_b,mouse_p,val):
    global text_alt
    for c in range(4):
        if text_data.text_base[alt][2+c] != '':
            pygame.draw.rect(janela, palette[p_checked][1], [direct_sizes[s_checked][6][0],direct_sizes[s_checked][6][1]+c*45,direct_sizes[s_checked][6][2],direct_sizes[s_checked][6][3]], False, 4)
            pygame.draw.rect(janela, palette[p_checked][6], [direct_sizes[s_checked][6][0],direct_sizes[s_checked][6][1]+c*45,direct_sizes[s_checked][6][2],direct_sizes[s_checked][6][3]], 1, 4)
            button_text = font_data.text_font.render(text_data.text_base[alt][2+c], True, palette[p_checked][3])
            janela.blit(button_text, (direct_sizes[s_checked][6][0] + direct_sizes[s_checked][6][2]/2 - button_text.get_size()[0]/2, direct_sizes[s_checked][6][1]+c*45 + direct_sizes[s_checked][6][3]/2 - button_text.get_size()[1]/2))
            if mouse_b[0] == True and  direct_sizes[s_checked][6][0]+direct_sizes[s_checked][6][2] >= mouse_p[0] >= direct_sizes[s_checked][6][0] and direct_sizes[s_checked][6][1]+c*45 + direct_sizes[s_checked][6][3] >= mouse_p[1] >= direct_sizes[s_checked][6][1]+c*45:
                chose.append(c)
                text_alt += 1
                return
    

def text_display(alt):
    global point
    global chose
    mouse_button = pygame.mouse.get_pressed()
    mouse_pos = pygame.mouse.get_pos()
    pygame.draw.rect(janela, palette[p_checked][1], direct_sizes[s_checked][7], False, 4)
    pygame.draw.rect(janela, palette[p_checked][6], direct_sizes[s_checked][7], 1, 4)
    # caixa de seleção de dialogos
    co = 0 
    
    for x in range(len(chose)):
        if type(gabarito[x]) == list:
            if chose[x] in gabarito[x]:
                co+=1
        elif chose[x] == gabarito[x]:
            co += 1
    point = co
    
    if text_data.text_base[alt][0] == 2:
        if text_data.text_base[alt][6] != '':
            pygame.draw.rect(janela, palette[p_checked][1], direct_sizes[s_checked][8], False, 4)
            pygame.draw.rect(janela, palette[p_checked][6], direct_sizes[s_checked][8], 1, 4)
            for c in range(len(text_data.text_base[alt])-6):
                text_box = font_data.text_font.render(text_data.text_base[alt][6+c], True, palette[p_checked][3])
                janela.blit(text_box,(direct_sizes[s_checked][9][0],direct_sizes[s_checked][9][1]+c*direct_sizes[s_checked][9][2]))
        diag_button(alt,mouse_button,mouse_pos,1)
        return

    # caixa de texto central, como as instruções por exemplo
    if text_data.text_base[alt][0] == 1:
        pygame.draw.rect(janela, palette[p_checked][1], direct_sizes[s_checked][10], False, 4)
        pygame.draw.rect(janela, palette[p_checked][6], direct_sizes[s_checked][10], 1, 4)
        text_line = font_data.text_font.render(text_data.text_base[alt][2], True, palette[p_checked][3])
        janela.blit(text_line,(direct_sizes[s_checked][11][0]-(text_line.get_size()[0]/2),direct_sizes[s_checked][11][1]))
        for c in range(len(text_data.text_base[alt])-3):
            text_box = font_data.text_font.render(text_data.text_base[alt][3+c], True, palette[p_checked][3])
            janela.blit(text_box,(direct_sizes[s_checked][12][0],direct_sizes[s_checked][12][1]+c*18))
        return
    # caixa de texto padrão
    text_interface_1 = font_data.text_font.render("Z - Prosseguir", True, palette[p_checked][3])
    text_line = font_data.text_font.render(text_data.text_base[alt][2], True, palette[p_checked][3])
    janela.blit(text_line,direct_sizes[s_checked][13])
    janela.blit(text_interface_1,direct_sizes[s_checked][14])
    pygame.draw.polygon(janela, palette[p_checked][5], direct_sizes[s_checked][1])
    pygame.draw.circle(janela, palette[p_checked][5], direct_sizes[s_checked][15][0], direct_sizes[s_checked][15][1])
    for c in range(len(text_data.text_base[alt])-3):
        if '*' in text_data.text_base[alt][3+c]:
            text_box = font_data.text_font.render(text_data.question_diag[len(chose)-1][chose[len(chose)-1]],True,palette[p_checked][3])
        else:
            text_box = font_data.text_font.render(text_data.text_base[alt][3+c], True, palette[p_checked][3])
        janela.blit(text_box,(direct_sizes[s_checked][16][0],direct_sizes[s_checked][16][1]+c*direct_sizes[s_checked][16][2]))


def main_menu():
    global p_checked
    global size_checked
    global chose
    global text_alt
    pygame.display.set_caption("Menu Principal")
    pygame.display.set_mode(direct_sizes[0][0])
    text_alt = 0
    chose = []
    b_select = 1
    num_b = 3
    if any(save_list):
        num_b = 4
        b_select = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_DOWN:
                    if b_select == 4:
                        if num_b == 4:
                            b_select = 1
                        else:
                            b_select = 2
                    else:
                        b_select += 1
                
                if event.key == K_UP:
                    if b_select == 1 and num_b == 4 or b_select == 0 or b_select == 2 and num_b == 3 or b_select == 1 and num_b == 3:
                        b_select = 4
                    else:
                        b_select -= 1

                if event.key == K_RETURN:
                    if b_select == 1:
                        load_screen()
                    if b_select == 2:
                        diag_test()
                    if b_select == 3:
                        config_screen()
                    if b_select == 4:
                        sys.exit()
        janela.fill(palette[p_checked][0])
        mouse_pos = pygame.mouse.get_pos()
        mouse_button = pygame.mouse.get_pressed()
        #desenhando o background
        pygame.draw.rect(janela, palette[p_checked][2], [0,0,220,600])
        pygame.draw.circle(janela, palette[p_checked][2], (119,150),215)
        pygame.draw.circle(janela, palette[p_checked][0], (287,490),165)

        #chamando os botões
        logo = font_data.logo_font.render('Ecomundo',True,palette[p_checked][2])
        janela.blit(logo,[350,100])
        button(60,80,[110,33],mouse_button,mouse_pos,diag_test,'Iniciar', b_select, 2)
        button(60,130,[110,33],mouse_button,mouse_pos,config_screen,'Configurações',b_select, 3)
        button(75,180,[80,25],mouse_button,mouse_pos,sys.exit,'Sair', b_select, 4)
        if num_b == 4:
            button(60,30,[110,33],mouse_button,mouse_pos,load_screen,'Continuar', b_select, 1)
        pygame.display.update()

def config_screen():
    pygame.display.set_caption("Configurações")
    b_select = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        janela.fill(palette[p_checked][0])
        mouse_pos = pygame.mouse.get_pos()
        mouse_button = pygame.mouse.get_pressed()
        
        rbs_function(480,65,mouse_button,mouse_pos,0)
        rbs_function(480,85,mouse_button,mouse_pos,1)
        rbs_function(480,105,mouse_button,mouse_pos,2)
        radiobutton(480,65,p_checked)
        radiobutton(480,85,p_checked)
        radiobutton(480,105,p_checked)
    
        pygame.draw.rect(janela, palette[p_checked][1], [janela.get_size()[0]*3/100,janela.get_size()[1]*60/100,janela.get_size()[0]*94/100,janela.get_size()[1]*25/100], False, 4)
        pygame.draw.rect(janela, palette[p_checked][6], [janela.get_size()[0]*3/100,janela.get_size()[1]*60/100,janela.get_size()[0]*94/100,janela.get_size()[1]*25/100], 1, 4)
        diag_ex = font_data.text_font.render('Lorem ipsum dolor sit amet, consectetur adipiscing elit.', True, palette[p_checked][3])
        janela.blit(diag_ex, (39,364))
        #textos 
        menu_text(352,5,'Configuração')        
        menu_text(48,34,'Temas')
        menu_text(488,34,'Resoluções')

        #radionbuttons e textos referentes a eles
        for c in range(len(palette)):
            menu_text(50,56+c*20,palette[c][7])
            rbp_function(40,65+c*20,mouse_button,mouse_pos,c)
            radiobutton(40,65+c*20,p_checked)
            
        menu_text(490,56, '800x600')
        menu_text(490,76, '950x720')
        menu_text(490,96, '1250x900')
        
        pygame.draw.circle(janela, palette[p_checked][1],(40,43), 3)
        pygame.draw.circle(janela, palette[p_checked][1],(480,43), 3)
        pygame.draw.polygon(janela, palette[p_checked][5], ((750,495),(755,500),(760,495)))
        pygame.draw.circle(janela, palette[p_checked][5], (33,373), 3)

        button(650,540,[90,27],mouse_button,mouse_pos,main_menu,'Confirmar',b_select, 1)
        #Trocar pela imagem do "i" de informações
        pygame.draw.rect(janela, (255,255,255), [95,35,10,15])
        if 95 <= mouse_pos[0] <= 105 and 35 <= mouse_pos[1] <= 50:
            text_intruction = font_data.obs_font.render('Os temas escuros são os mais recomendados para monitores OLED', True, palette[p_checked][3], palette[p_checked][1])
            janela.blit(text_intruction,(15,27))

        pygame.display.update()


def diag_test():
    global text_alt
    global chose
    global point
    pygame.display.set_caption("Ecomundo")
    pygame.display.set_mode(direct_sizes[s_checked][0])
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN and text_data.text_base[text_alt][0] != 2 and direct_sizes[s_checked][7][0]<=mouse_pos[0]<=direct_sizes[s_checked][7][0] + direct_sizes[s_checked][7][2] and direct_sizes[s_checked][7][1] <= mouse_pos[1] <= direct_sizes[s_checked][7][1]+direct_sizes[s_checked][7][3]:
                text_alt += 1
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    backlog_menu()
            if event.type == pygame.KEYUP and text_data.text_base[text_alt][0] != 2:
                if event.key == K_z:
                    text_alt += 1
                if event.key == K_SPACE:
                    text_alt += 1
        pygame.time.delay(30)
        if text_alt == len(text_data.text_base) and len(text_data.text_base) > 17:
            while len(text_data.text_base) > 17:
                text_data.text_base.pop(-1)
            main_menu()
        re_bg = pygame.transform.smoothscale(back_grounds[text_data.text_base[text_alt][1]], [janela.get_size()[0],janela.get_size()[1]])
        janela.blit(re_bg,(0,0))
        if text_data.text_base[text_alt][1] < 2:
            if text_alt >= 16:
                if point >= 4:
                    if len(text_data.text_base) <= 18: 
                        for c in text_data.plot_good:
                            text_data.text_base.append(c)
                    resize = pygame.transform.smoothscale(char_sprite[1], [100+(s_checked*35),250+(s_checked*35)])
                elif point >= 2:
                    if len(text_data.text_base) <= 18: 
                        for c in text_data.plot_neutral:
                            text_data.text_base.append(c)
                    resize = pygame.transform.smoothscale(char_sprite[0], [100+(s_checked*35),250+(s_checked*35)])
                elif point <= 1:
                    if len(text_data.text_base) <= 18:
                        for c in text_data.plot_bad:
                            text_data.text_base.append(c)
                    resize = pygame.transform.smoothscale(char_sprite[2], [100+(s_checked*35),250+(s_checked*35)])
            else:
                resize = pygame.transform.smoothscale(char_sprite[0], [100+(s_checked*35),250+(s_checked*35)])
            janela.blit(resize, direct_sizes[s_checked][17])
        
        text_display(text_alt)
        mouse_pos = pygame.mouse.get_pos()
        # outra forma de mapear botões do teclado
        key_press = pygame.key.get_pressed()
        if text_data.text_base[text_alt][0] == 0:
            if key_press[122] or key_press[32]:
                pygame.draw.polygon(janela, palette[p_checked][3], (direct_sizes[s_checked][1]))
        pygame.display.update()
        janela.fill(palette[p_checked][0])

  
chose = []
gabarito = [[1,2],[1,2],0,3,0]
point = 0
char_sprite = []
for fn in glob.iglob("**/sprites" + '**/*.png', recursive=True):
    char_sprite.append(pygame.image.load(fn))
back_grounds = []
for fn in glob.iglob("**/backg" + '**/*.png', recursive=True):
    back_grounds.append(pygame.image.load(fn))
text_alt = 0
palette = [([220,220,220],[130,130,130],[88,88,88],[30,30,30],[130,130,130],[88,88,88],[0,0,0],"Padrão"),
([33, 104, 105],[31, 36, 33],[31, 36, 33],[16, 240, 177],[33, 104, 105],[192, 253, 255],[156, 197, 161],"Verde Natureza"),
([33, 37, 41],[108, 117, 125],[222, 170, 255],[222, 170, 255],[73, 80, 87],[208, 209, 255],[248, 249, 250],"Pastel Grey"),
([0, 100, 148],[5, 25, 35],[5, 130, 202],[0, 166, 251],[0, 53, 84],[5, 130, 202],[0, 166, 251],"Ocean"),
([11, 19, 43],[33, 47, 69],[0, 100, 102],[0,255,213],[27, 58, 75],[0, 100, 102],[0, 100, 102],"Deep Ocean"),
([54, 21, 30],[68, 85, 82],[165, 196, 212],[248, 243, 43],[165, 196, 212],[248, 243, 43],[248, 243, 43],"Retrô"),
([105, 48, 195],[137, 228, 245],[86, 0, 154],[255, 14, 255],[105, 48, 195],[86, 207, 225],[255, 103, 237],"Rosa e Roxo"),
([0, 53, 102],[255, 214, 10],[0, 8, 20],[0, 8, 20],[255, 195, 0],[0, 53, 102],[0, 8, 20],"Amarelo e Azul"),
([3, 7, 30],[220, 47, 2],[157, 2, 8],[250, 173, 7],[218, 25, 2],[157, 2, 8],[250, 173, 7],"Chama"),
([51, 204, 51],[112, 224, 0],[0, 75, 35],[0, 75, 35],[92, 204, 0],[56, 176, 0],[0, 75, 35],"Verde Claro"),
([20, 218, 225],[163, 247, 181],[255, 200, 221],[0, 95, 115],[10, 147, 150],[255, 179, 193],[255, 179, 193],"Verde Água"),
([192, 253, 255],[224, 170, 255],[216, 187, 255],[36, 0, 70],[216, 187, 255],[199, 125, 255],[157, 78, 221],"Pastel"),
([10,25,78],[230,30,140],[85,85,255],[255,255,255],[0,20,255],[85,85,255],[85,85,255],"Azul e Rosa"),
([100,100,100],[20,20,20],[20,20,20],[0,255,163],[65,65,65],[0,255,213],[0,255,213],"Green-Cyber")]
p_checked = 4
'''
0 cor do background
1 cor do botão comum/contorno do radiobutton/fundo da caixa de dialogo
2 detalhe do menu principal
3 seleção do radiobutton/cor das letras/  cor de destaque do triângulo quando clica Z
4 Cor de seleção do botão comum
5 detalhes do painel de texto  (triângulo do proximo, e bolinha do nome), se der colocar um diferente do 3
6 cor do contorno das caixas de dialogo, e detalhes do contorno dos botões comuns
7 Nome
'''
direct_sizes  = [([800,600],[(630,575),(635,580),(640,575)],[30,500,(60,30)],[0,0,220,600],[(119,150),(287,490)],[215,165],[200,250,400,35],[24,438,752,150],[250,50,300,180],[261,60,18],
[250,150,300,180],[400,153],[261,175],[42,438],[647,568],[(34.4,448.2),3],[32,456,18],  (351,105)),

([950,720],[(780,695),(785,700),(790,695)],[35,600,(60,30)],[0,0,261,720],[(140,178),(344,587)],[251,207],[200,260,550,35],[35,560,880,150],[325,60,300,180],[336,65,18],
[325,180,300,180],[475,183],[336,205],[52,560],[798,689],[(45.4,570.2),3],[41,578,18],  (410,142)),

([1250,900],[(1080,877),(1085,882),(1090,877)],[40,738,(60,30)],[0,0,342,900],[(170,227),(413,755)],[325,262],[350,310,550,35],[35,740,1180,150],[475,110,300,180],[486,115,18],
[475,200,300,180],[625,203],[486,225],[54,740],[1097,870],[(46,750),3],[42,760,18], (540,213))]
s_checked = 1


with open('saves.pkl','rb') as c:
    save_list = pickle.load(c)
    c.close()

'''
tamanho da janela = 0
triangulo do chat = 1
botão backlog = 2
desenho de fundo do backlog = 3 - 4 - 5
botão de decisão do dialogo = 6
caixa de dialogo = 7
caixa de dialogo central de decisões = 8
texto da caixa de dialogo central de decisões = 9
caixa de dialogo central introdução = 10
texto do titulo da caixa de dialogo central introdução = 11
texto normal da caixa de dialogo central introdução = 12
"nome" na caixa de dialogo = 13
"Z - Prosseguir" = 14
circulo antes do nome da caixa de dialogo = 15
direção do texto base = 16
as 2 ou 4 posições possiveis dos personagens = 18
botão de save = 19
'''
janela = pygame.display.set_mode((800,600))
