#Fliperama em C++ (MeuApp v4.0)

## O que e
O programa ele roda adivinhe o numero e mostra os jogadores salvos e quantas partidas e que jogaram 

## Como compilar e rodar
g++ -Wall fliperama.cpp -o fliperama 
./fliperama

## Arquivos
fliperama.cpp void mostrar_menu() {
    linha();
    cout << "  FLIPERAMA DO " << DONO << endl;
    linha();
    cout << "[1] Adivinhe o Numero" << endl;
    cout  << "[2] Cadastrar jogadores" << endl;
    cout << "[3] Listar jogadores" << endl;
    cout << "[0] Sair" << endl;
    linha();
}

jogadores.csv opcao = ler_numero("Sua escolha", 0, 3);
    while (opcao != 0) {
        if (opcao == 1) {
            jogar_adivinhe(apelidos, partidas);
        } else if (opcao == 2) {
            cadastrar(apelidos, partidas);
        } else {
            listar(apelidos, partidas);
        }
        mostrar_menu();
        opcao = ler_numero("Sua escolha",0, 3);

        ## C x c++: o que mudou
        mudou os comandos mas ainda fazem a mesma funcao so que em estilos diferentes 

        ## O que o C++ decidiu por mim 
        alguns comandos que ele pede pra mudar porque fica dando erro

        ## Autoavaliacao 
        Bom eu acho que fui bem fiz todos os comandos que pedia e está rodando, entao espero um B 