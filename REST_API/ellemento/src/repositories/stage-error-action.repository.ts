import {inject, Getter} from '@loopback/core';
import {DefaultCrudRepository, repository, HasOneRepositoryFactory} from '@loopback/repository';
import {EllementoDbDataSource} from '../datasources';
import {StageErrorAction, StageErrorActionRelations, ErrorType} from '../models';
import {ErrorTypeRepository} from './error-type.repository';

export class StageErrorActionRepository extends DefaultCrudRepository<
  StageErrorAction,
  typeof StageErrorAction.prototype.id,
  StageErrorActionRelations
> {

  public readonly errorType: HasOneRepositoryFactory<ErrorType, typeof StageErrorAction.prototype.error_type_id>;

  constructor(
    @inject('datasources.ellemento_db') dataSource: EllementoDbDataSource, @repository.getter('ErrorTypeRepository') protected errorTypeRepositoryGetter: Getter<ErrorTypeRepository>,
  ) {
    super(StageErrorAction, dataSource);
    this.errorType = this.createHasOneRepositoryFactoryFor('errorType', errorTypeRepositoryGetter);
    this.registerInclusionResolver('errorType', this.errorType.inclusionResolver);
  }
}
