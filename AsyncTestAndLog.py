
import time
import asyncio
import concurrent.futures
import logging
import logging.config
import yaml

def execute_teste(nome):
    '''
    teste lento
    '''
    log = logging.getLogger(__name__)
    for valor in range(5):
        log.info('LENTO {0} v:{1}'.format(nome, valor))
        time.sleep(0.25)
        
    return nome 

async def main(log):
    log.info("Main Start")  
    loop = asyncio.get_event_loop()
    with concurrent.futures.ThreadPoolExecutor(max_workers=20, thread_name_prefix='paralelo') as executor:

        blocos_tarefa = [loop.run_in_executor(executor, execute_teste, 'thread-' + str(val)) for val in range(50)]
        tam = len(blocos_tarefa)
        while tam > 0:
            done, pending = await asyncio.wait(blocos_tarefa)# = await asyncio.wait(blocos)

            for encerrado in done:
                log.info('REPOSTA VAL: {0}'.format(encerrado.result()))
                blocos_tarefa.remove(encerrado)

            log.info('Tamanho bloco:' + str(len(blocos_tarefa)))
            tam = len(blocos_tarefa)

    log.info("Main End")

def setloger(config_file):
    with open(config_file) as stream:
        try:
            global_config = yaml.load(stream)
            dados_log = global_config['loggin']
            
            logging.config.dictConfig(dados_log)
            log = logging.getLogger(__name__)
            log.info("logger Iniciado")
            return log

        except yaml.YAMLError as exc:
            print(exc)
            quit()

if __name__ == '__main__':
    
    log = setloger("config.yaml")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(log))
    log.info('FIM')
    