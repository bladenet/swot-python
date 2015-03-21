import re
import tldextract
from os.path import join, dirname, exists

BLACKLIST = frozenset([
    'si.edu',
    'america.edu',
    'californiacolleges.edu',
    'australia.edu',
    'cet.edu'
])

ACADEMIC_TLDS = frozenset([
    'ac.ae',
    'ac.at',
    'ac.bd',
    'ac.be',
    'ac.cn',
    'ac.cr',
    'ac.cy',
    'ac.fj',
    'ac.gg',
    'ac.gn',
    'ac.id',
    'ac.il',
    'ac.in',
    'ac.ir',
    'ac.jp',
    'ac.ke',
    'ac.kr',
    'ac.ma',
    'ac.me',
    'ac.mu',
    'ac.mw',
    'ac.mz',
    'ac.ni',
    'ac.nz',
    'ac.om',
    'ac.pa',
    'ac.pg',
    'ac.pr',
    'ac.rs',
    'ac.ru',
    'ac.rw',
    'ac.sz',
    'ac.th',
    'ac.tz',
    'ac.ug',
    'ac.uk',
    'ac.yu',
    'ac.za',
    'ac.zm',
    'ac.zw',
    'ed.ao',
    'ed.cr',
    'ed.jp',
    'edu',
    'edu.af',
    'edu.al',
    'edu.ar',
    'edu.au',
    'edu.az',
    'edu.ba',
    'edu.bb',
    'edu.bd',
    'edu.bh',
    'edu.bi',
    'edu.bn',
    'edu.bo',
    'edu.br',
    'edu.bs',
    'edu.bt',
    'edu.bz',
    'edu.ck',
    'edu.cn',
    'edu.co',
    'edu.cu',
    'edu.do',
    'edu.dz',
    'edu.ec',
    'edu.ee',
    'edu.eg',
    'edu.er',
    'edu.es',
    'edu.et',
    'edu.ge',
    'edu.gh',
    'edu.gr',
    'edu.gt',
    'edu.hk',
    'edu.hn',
    'edu.ht',
    'edu.in',
    'edu.iq',
    'edu.jm',
    'edu.jo',
    'edu.kg',
    'edu.kh',
    'edu.kn',
    'edu.kw',
    'edu.ky',
    'edu.kz',
    'edu.la',
    'edu.lb',
    'edu.lr',
    'edu.lv',
    'edu.ly',
    'edu.me',
    'edu.mg',
    'edu.mk',
    'edu.ml',
    'edu.mm',
    'edu.mn',
    'edu.mo',
    'edu.mt',
    'edu.mv',
    'edu.mw',
    'edu.mx',
    'edu.my',
    'edu.ni',
    'edu.np',
    'edu.om',
    'edu.pa',
    'edu.pe',
    'edu.ph',
    'edu.pk',
    'edu.pl',
    'edu.pr',
    'edu.ps',
    'edu.pt',
    'edu.pw',
    'edu.py',
    'edu.qa',
    'edu.rs',
    'edu.ru',
    'edu.sa',
    'edu.sc',
    'edu.sd',
    'edu.sg',
    'edu.sh',
    'edu.sl',
    'edu.sv',
    'edu.sy',
    'edu.tr',
    'edu.tt',
    'edu.tw',
    'edu.ua',
    'edu.uy',
    'edu.ve',
    'edu.vn',
    'edu.ws',
    'edu.ye',
    'edu.zm',
    'es.kr',
    'g12.br',
    'hs.kr',
    'ms.kr',
    'sc.kr',
    'sc.ug',
    'sch.ae',
    'sch.gg',
    'sch.id',
    'sch.ir',
    'sch.je',
    'sch.jo',
    'sch.lk',
    'sch.ly',
    'sch.my',
    'sch.om',
    'sch.ps',
    'sch.sa',
    'sch.uk',
    'school.nz',
    'school.za',
    'vic.edu.au'
])


class Swot(object):
    @classmethod
    def is_academic(cls, domain_str):
        if not domain_str or not isinstance(domain_str, (str, unicode)):
            return False

        domain_str = domain_str.strip().lower()
        domain = tldextract.extract(domain_str)
        if not domain.registered_domain:
            return False

        if [b for b in BLACKLIST if re.search(r'(\A|\.){}'.format(re.escape(b)), domain_str)]:
            return False

        if domain.tld in ACADEMIC_TLDS:
            return True

        if Swot.__is_academic_domain(domain):
            return True

        return False

    @classmethod
    def __is_academic_domain(cls, domain):
        path = join(dirname(__file__), 'data/lib/domains', join(*reversed(domain.registered_domain.split('.'))))
        domain_file = '{}.txt'.format(path)
        return exists(domain_file)


if __name__ == '__main__':
    import sys

    print Swot.is_academic(sys.argv[1])
