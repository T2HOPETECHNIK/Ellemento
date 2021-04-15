import {inject, Getter} from '@loopback/core';
import {DefaultCrudRepository, repository, HasManyRepositoryFactory} from '@loopback/repository';
import {EllementoDbDataSource} from '../datasources';
import {ErrorType, ErrorTypeRelations, History} from '../models';
import {HistoryRepository} from './history.repository';

export class ErrorTypeRepository extends DefaultCrudRepository<
  ErrorType,
  typeof ErrorType.prototype.error_type_id,
  ErrorTypeRelations
> {

  public readonly histories: HasManyRepositoryFactory<History, typeof ErrorType.prototype.error_type_id>;

  constructor(
    @inject('datasources.ellemento_db') dataSource: EllementoDbDataSource, @repository.getter('HistoryRepository') protected historyRepositoryGetter: Getter<HistoryRepository>,
  ) {
    super(ErrorType, dataSource);
    this.histories = this.createHasManyRepositoryFactoryFor('histories', historyRepositoryGetter,);
    this.registerInclusionResolver('histories', this.histories.inclusionResolver);
  }
}
