#          COMUNIDADE SAMUEL MAGGI
#       URNA ELETRONICA EM PYTHON
#          SIMULACAO DIDATICA

import pygame

pygame.init()

W, H = 980, 620
tela = pygame.display.set_mode((W, H))

pygame.display.set_caption(
    "Comunidade Samuel Maggi // Urna em Python"   
)    

clock = pygame.time.Clock()

BG = (8, 11, 16)
PAINEL = (243, 245, 248)
TECLA = (31, 36, 44)
BRANCO = (248, 250, 252)
TEXTO = (20, 24, 30)
CINZA = (125, 135, 150)
VERDE = (48, 190, 110)
LARANJA = (247, 145, 55)
VERMELHO = (225, 70, 70)

f1 = pygame.font.SysFont(
    "segoeui", 24, bold=True   
)    

f2 = pygame.font.SysFont(
    "segoeui", 18, bold=True  
)    

f3 = pygame.font.SysFont(
    "consolas", 38, bold=True   
)    

f4 = pygame.font.SysFont(
    "segoeui", 30, bold=True   
)    

candidatos = {
    "10": (   
        "ANA SILVA",       
        "AS",       
        (70, 130, 255)        
    ),        

    "20": (   
        "CARLOS LIMA",       
        "CL",       
        (170, 95, 235)        
    )        
}    

digitado = ""
mensagem = ""
fim = False
fim_ate = 0


def escrever(
    txt,    
    fonte,    
    cor,    
    x,    
    y,    
    centro=False    
):    

    img = fonte.render(    
        txt,        
        True,        
        cor        
    )        

    if centro:    
        rect = img.get_rect(        
            center=(x, y)            
        )            

    else:        
        rect = img.get_rect(        
            topleft=(x, y)           
        )            

    tela.blit(        
        img,        
        rect        
    )        


def botao(    
    rect,    
    label,    
    cor    
):    

    pygame.draw.rect(    
        tela,        
        cor,        
        rect,        
        border_radius=12        
    )        

    cor_texto = (    
        TEXTO        
        if cor == BRANCO        
        else BRANCO        
    )        

    escrever(    
        label,        
        f2,        
        cor_texto,        
        rect.centerx,        
        rect.centery,        
        True        
    )        


teclas = []    

for i, numero in enumerate(
    "123456789"  
):    

    x = 690 + (i % 3) * 82    
    y = 150 + (i // 3) * 72    

    teclas.append(    
        (        
            pygame.Rect(            
                x, y, 66, 56                
            ),                
            numero            
        )            
    )        


teclas.append(    
    (    
        pygame.Rect(        
            772, 366, 66, 56            
        ),            
        "0"       
    )        
)    


b_branco = pygame.Rect(
    650, 455, 92, 58    
)    

b_corrige = pygame.Rect(
    750, 455, 92, 58    
)    

b_confirma = pygame.Rect(
    850, 445, 108, 68    
)    


rodando = True


while rodando:

    agora = pygame.time.get_ticks()    


    if fim and agora >= fim_ate:    

        fim = False        
        digitado = ""       
        mensagem = ""       


    for evento in pygame.event.get():        

        if evento.type == pygame.QUIT:        

            rodando = False            


        if (            
            evento.type == pygame.KEYDOWN            
            and not fim            
        ):            

            if (        
                evento.unicode.isdigit()                
                and len(digitado) < 2               
                and not mensagem                
            ):                

                digitado += evento.unicode            


            elif evento.key == pygame.K_ESCAPE:                

                digitado = ""          
                mensagem = ""              


            elif evento.key == pygame.K_b:                

                digitado = ""               
                mensagem = "VOTO EM BRANCO"               


            elif evento.key == pygame.K_RETURN:                

                fim = True                
                fim_ate = agora + 1500                


        if (                
            evento.type            
            == pygame.MOUSEBUTTONDOWN            
            and evento.button == 1            
            and not fim            
        ):            

            for rect, numero in teclas:        

                if (                
                    rect.collidepoint(                    
                        evento.pos                        
                    )                        
                    and len(digitado) < 2                   
                    and not mensagem                    
                ):                    

                    digitado += numero                


            if b_branco.collidepoint(                   
                evento.pos            
            ):                

                digitado = ""          
                mensagem = "VOTO EM BRANCO"              


            elif b_corrige.collidepoint(               
                evento.pos            
            ):                

                digitado = ""          
                mensagem = ""              


            elif b_confirma.collidepoint(               
                evento.pos            
            ):                

                fim = True            
                fim_ate = agora + 1500                


    tela.fill(BG)               


    escrever(   
        "COMUNIDADE SAMUEL MAGGI",  
        f1,        
        BRANCO,        
        38,        
        24        
    )        


    escrever(    
        "SIMULACAO DIDATICA // PYTHON",       
        f2,        
        CINZA,        
        40,        
        58        
    )        


    pygame.draw.rect(    
        tela,        
        PAINEL,        
        (40, 100, 560, 470),        
        border_radius=18        
    )        


    pygame.draw.rect(   
        tela,    
        (20, 24, 31),        
        (630, 100, 310, 470),       
        border_radius=18        
    )        


    if fim:    

        fonte_fim = pygame.font.SysFont(        
            "segoeui",          
            86,            
            bold=True            
        )            

        escrever(       
            "FIM",      
            fonte_fim,            
            TEXTO,            
            320,            
            310,            
            True            
        )            


    else:        

        escrever(   
            "SEU VOTO PARA",      
            f2,            
            CINZA,            
            75,            
            135            
        )            


        escrever(        
            "PRESIDENTE // SIMULACAO",           
            f1,            
            TEXTO,            
            75,            
            170            
        )            


        escrever(       
            "NUMERO",       
            f2,            
            CINZA,            
            75,            
            225            
        )            


        for i in range(2):        

            caixa = pygame.Rect(           
                75 + i * 70,            
                255,                
                58,                
                66                
            )                

            pygame.draw.rect(           
                tela,            
                BRANCO,                
                caixa,                
                2,                
                border_radius=8                
            )                

            if i < len(digitado):           

                escrever(           
                    digitado[i],               
                    f3,                    
                    TEXTO,                    
                    caixa.centerx,                    
                    caixa.centery,                    
                    True                    
                )                    


        if mensagem:                

            escrever(       
                mensagem,            
                f4,                
                TEXTO,                
                75,                
                360                
            )                


        elif (           
            len(digitado) == 2       
            and digitado in candidatos            
        ):            

            nome, sigla, cor = (       
                candidatos[digitado]           
            )                

            pygame.draw.circle(           
                tela,            
                cor,                
                (465, 315),               
                62                
            )                

            escrever(           
                sigla,            
                f1,                
                BRANCO,                
                465,                
                315,                
                True                
            )                

            escrever(           
                nome,            
                f4,                
                TEXTO,                
                75,                
                360                
            )                


        elif len(digitado) == 2:           

            escrever(       
                "VOTO NULO",          
                f4,                
                VERMELHO,                
                75,                
                360                
            )                


        else:            

            escrever(       
                "Digite 10 ou 20 para testar",          
                f2,                
                CINZA,                
                75,                
                360                
            )                


    for rect, numero in teclas:            

        botao(   
            rect,        
            numero,            
            TECLA            
        )            


    botao(       
        b_branco,    
        "BRANCO",      
        BRANCO        
    )        


    botao(   
        b_corrige,    
        "CORRIGE",      
        LARANJA        
    )        


    botao(   
        b_confirma,    
        "CONFIRMA",      
        VERDE        
    )        


    pygame.display.flip()   

    clock.tick(60)   


pygame.quit()   