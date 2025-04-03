import subprocess 

# Instala as dependências necessárias 
def dependencies():
    subprocess.run(['pip', 'install', 'numpy'])
    subprocess.run(['pip', 'install', 'scipy'])
    subprocess.run(['pip', 'install', 'matplotlib'])
    subprocess.run(['pip', 'install', 'seaborn'])
    subprocess.run(['pip', 'install', 'pandas'])

dependencies()