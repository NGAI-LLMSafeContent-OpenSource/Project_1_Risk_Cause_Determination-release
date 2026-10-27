"""Exercise the published ValueQA code/contracts without CUDA or production API keys."""
from pathlib import Path
import json
import os
import re
import subprocess
import sys
import tempfile
import venv

ROOT=Path(__file__).resolve().parents[1]

def main():
    if sys.version_info<(3,10):raise RuntimeError('Python >=3.10 is required')
    env={k:v for k,v in os.environ.items() if k in ('PATH','HOME','SYSTEMROOT','SystemRoot','WINDIR','TEMP','TMP','LANG','LC_ALL','SSL_CERT_FILE','SSL_CERT_DIR')}
    env['NO_PROXY']='127.0.0.1,localhost,::1';env['no_proxy']=env['NO_PROXY']
    summaries=[]
    with tempfile.TemporaryDirectory(prefix='valueqa-release-check-') as tmp:
        directory=Path(tmp)/'venv';venv.EnvBuilder(with_pip=False).create(directory)
        python=directory/('Scripts/python.exe' if os.name=='nt' else 'bin/python')
        def run(argv):
            result=subprocess.run([str(x) for x in argv],cwd=ROOT,env=env,capture_output=True,text=True,timeout=300)
            print(result.stdout,flush=True);print(result.stderr,file=sys.stderr,flush=True)
            if result.returncode:raise RuntimeError('Release check failed: '+' '.join(map(str,argv)))
            return result.stdout+result.stderr
        run([sys.executable,'-m','pip','--isolated','--python',python,'install','--no-cache-dir','-r',ROOT/'requirements.txt'])
        run([python,'-B','ValueQA_Classification/verify_version.py'])
        for argv in [[python,'-B','-m','unittest','discover','-s','tests','-p','test_valueqa_classification_integration.py'],[python,'-B','-m','unittest','ValueQA_Classification.test_framework']]:
            output=run(argv);counts=re.findall(r'Ran (\d+) tests?',output)
            summaries.append({'command':[str(x) for x in argv[2:]],'passed_tests':int(counts[-1]) if counts else None})
        run([python,'-B','tools/run.py','--help'])
    print(json.dumps({'passed':True,'scope':'CPU contracts, rules, runner/CLI and local mock HTTP only; no real-model inference or accuracy validation','tests':summaries},ensure_ascii=False))

if __name__=='__main__':main()
