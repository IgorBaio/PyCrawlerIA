create database indice;
use indice;

create table urls(
    idUrl int not null auto_increment,
    url varchar(1000) not null,
    constraint pk_urls_idUrl primary key (idUrl)
);

create index idx_urls_url on urls(url);

create table palavras(
    idPalavra int not null auto_increment,
    palavra varchar(200) not null,
    constraint pk_palavras_palavra primary key (idPalavra)
);

create index idx_palavras_palavra on palavras(palavra);

create table palavra_localizacao(
    idPalavra_localizacao int not null auto_increment,
    idUrl int not null,
    idPalavra int not null,
    localizacao int not null,
    constraint pk_idPalavra_localizacao_ primary key (idPalavra_localizacao),
    constraint fk_palavra_localizacao_idUrl foreign key (idUrl) references urls(idUrl),
    constraint fk_palavra_localizacao_idPalavra foreign key (idPalavra) references palavras(idPalavra)
);

create index idx_palavra_localizacao_idPalavra on palavra_localizacao(idPalavra);


alter database indice character set = utf8mb4 collate = utf8mb4_unicode_ci ;
alter table palavras convert to character set utf8mb4 collate utf8mb4_unicode_ci;
alter table palavras modify column palavra varchar(200) character set utf8mb4 collate utf8mb4_unicode_ci;